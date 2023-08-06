import copy
import logging

from flask import current_app, url_for, request, abort, session, redirect, Response
from flask_login import logout_user, current_user, login_required
from flask.views import MethodView

from saml2 import BINDING_HTTP_POST, BINDING_HTTP_REDIRECT
from saml2.authn_context import PASSWORD, AuthnBroker, authn_context_class_ref
from saml2.config import IdPConfig
from saml2.ident import NameID
from saml2.metadata import entity_descriptor
from saml2.s_utils import UnknownPrincipal, UnsupportedBinding
from saml2.saml import NAMEID_FORMAT_UNSPECIFIED
from saml2.server import Server

from .processors import BaseProcessor
from .util import import_string, never_cache

logger = logging.getLogger(__name__)


@never_cache
def sso_entry():
    """ Entrypoint view for SSO. Gathers the parameters from the HTTP request, stores them in the session
        and redirects the requester to the login_process view.
    """
    if request.method == 'POST':
        passed_data = request.form
        binding = BINDING_HTTP_POST
    else:
        passed_data = request.args
        binding = BINDING_HTTP_REDIRECT

    session['Binding'] = binding

    try:
        session['SAMLRequest'] = passed_data['SAMLRequest']
    except KeyError:
        return abort(400)

    session['RelayState'] = passed_data.get('RelayState', '')

    # TODO check how the redirect saml way works. Taken from example idp in pysaml2.
    if "SigAlg" in passed_data and "Signature" in passed_data:
        session['SigAlg'] = passed_data['SigAlg']
        session['Signature'] = passed_data['Signature']
    return redirect(url_for('flasksaml2idp.saml_login_process'))


class IdPHandlerViewMixin:
    """ Contains some methods used by multiple views """
    decorators = [never_cache]
    error_func = None

    def __init__(self, *args, **kwargs):
        self.error_func = import_string(getattr(current_app.config, 'SAML_IDP_ERROR_VIEW_FUNC',
                                        'flasksaml2idp.error_views.saml_IDP_error_view'))
        return super(IdPHandlerViewMixin, self).__init__(*args, **kwargs)

    def handle_error(self, **kwargs):
        return self.error_func(**kwargs)

    def dispatch_request(self, *args, **kwargs):
        """ Construct IDP server with config from settings dict
        """
        conf = IdPConfig()
        try:
            conf.load(copy.deepcopy(current_app.config['SAML_IDP_CONFIG']))
            self.IDP = Server(config=conf)
        except Exception as e:
            return self.handle_error(request, exception=e)
        return super(IdPHandlerViewMixin, self).dispatch_request(*args, **kwargs)

    def get_processor(self, entity_id, sp_config):
        """ Instantiate user-specified processor or default to an all-access base processor.
            Raises an exception if the configured processor class can not be found or initialized.
        """
        processor_string = sp_config.get('processor', None)
        if processor_string:
            try:
                return import_string(processor_string)(entity_id)
            except Exception as e:
                logger.error("Failed to instantiate processor: {} - {}".format(processor_string, e), exc_info=True)
                raise
        return BaseProcessor(entity_id)

    def get_identity(self, processor, user, sp_config):
        """ Create Identity dict (using SP-specific mapping)
        """
        sp_mapping = sp_config.get('attribute_mapping', {'username': 'username'})
        return processor.create_identity(user, sp_mapping, **sp_config.get('extra_config', {}))


class LoginProcessView(IdPHandlerViewMixin, MethodView):
    """ View which processes the actual SAML request and returns a self-submitting form with the SAML response.
        The login_required decorator ensures the user authenticates first on the IdP using 'normal' ways.
    """
    decorators = [never_cache, login_required]

    def get(self, *args, **kwargs):
        binding = session.get('Binding', BINDING_HTTP_POST)

        # Parse incoming request
        try:
            req_info = self.IDP.parse_authn_request(session['SAMLRequest'], binding)
        except Exception as excp:
            return self.handle_error(exception=excp)

        # Signed request for HTTP-REDIRECT
        if "SigAlg" in session and "Signature" in session:
            _certs = self.IDP.metadata.certs(req_info.message.issuer.text, "any", "signing")
            verified_ok = False
            for cert in _certs:
                # TODO implement
                # if verify_redirect_signature(_info, self.IDP.sec.sec_backend, cert):
                #    verified_ok = True
                #    break
                pass
            if not verified_ok:
                return self.handle_error(request, extra_message="Message signature verification failure", status=400)

        # Gather response arguments
        try:
            resp_args = self.IDP.response_args(req_info.message)
        except (UnknownPrincipal, UnsupportedBinding) as excp:
            return self.handle_error(exception=excp, status=400)

        try:
            sp_config = current_app.config['SAML_IDP_SPCONFIG'][resp_args['sp_entity_id']]
        except Exception:
            # TODO Inproper config exception
            return self.handle_error(exception=Exception("No config for SP %s defined in SAML_IDP_SPCONFIG"
                                                         % resp_args['sp_entity_id']),
                                     status=400)

        processor = self.get_processor(resp_args['sp_entity_id'], sp_config)

        # Check if user has access to the service of this SP
        if not processor.has_access(request):
            # TODO PermissionDenied Exception
            return self.handle_error(exception=Exception("You do not have access to this resource"),
                                     status=403)

        identity = self.get_identity(processor, request.user, sp_config)

        req_authn_context = req_info.message.requested_authn_context or PASSWORD
        AUTHN_BROKER = AuthnBroker()
        AUTHN_BROKER.add(authn_context_class_ref(req_authn_context), "")

        user_id = processor.get_user_id(request.user)

        # Construct SamlResponse message
        try:
            authn_resp = self.IDP.create_authn_response(
                identity=identity, userid=user_id,
                name_id=NameID(format=resp_args['name_id_policy'].format, sp_name_qualifier=resp_args['sp_entity_id'],
                               text=user_id),
                authn=AUTHN_BROKER.get_authn_by_accr(req_authn_context),
                sign_response=self.IDP.config.getattr("sign_response", "idp") or False,
                sign_assertion=self.IDP.config.getattr("sign_assertion", "idp") or False,
                **resp_args)
        except Exception as excp:
            return self.handle_error(exception=excp, status=500)

        http_args = self.IDP.apply_binding(
            binding=resp_args['binding'],
            msg_str="%s" % authn_resp,
            destination=resp_args['destination'],
            relay_state=session['RelayState'],
            response=True)

        logger.debug('http args are: %s' % http_args)

        return self.render_response(processor, http_args)

    def render_response(self, processor, http_args):
        """ Return either as redirect to MultiFactorView or as html with self-submitting form.
        """
        if processor.enable_multifactor(current_user):
            # Store http_args in session for after multi factor is complete
            session['saml_data'] = http_args['data']
            logger.debug("Redirecting to process_multi_factor")
            return redirect(url_for('flasksaml2idp.saml_multi_factor'))
        logger.debug("Performing SAML redirect")
        return Response(http_args['data'])


class SSOInitView(IdPHandlerViewMixin, MethodView):

    decorators = [never_cache, login_required]

    def post(self, *args, **kwargs):
        return self.get(*args, **kwargs)

    def get(self, *args, **kwargs):
        passed_data = request.form if request.method == 'POST' else request.args

        # get sp information from the parameters
        try:
            sp_entity_id = passed_data['sp']
        except KeyError as excp:
            return self.handle_error(exception=excp, status=400)

        try:
            sp_config = current_app.config['SAML_IDP_SPCONFIG'].SAML_IDP_SPCONFIG[sp_entity_id]
        except Exception:
            # TODO improperly configured exception
            return self.handle_error(exception=Exception("No config for SP %s defined in SAML_IDP_SPCONFIG"
                                                         % sp_entity_id),
                                     status=400)

        binding_out, destination = self.IDP.pick_binding(
            service="assertion_consumer_service",
            entity_id=sp_entity_id)

        processor = self.get_processor(sp_entity_id, sp_config)

        # Check if user has access to the service of this SP
        if not processor.has_access():
            # TODO permission denied exception
            return self.handle_error(exception=Exception("You do not have access to this resource"),
                                     status=403)

        identity = self.get_identity(processor, current_user, sp_config)

        req_authn_context = PASSWORD
        AUTHN_BROKER = AuthnBroker()
        AUTHN_BROKER.add(authn_context_class_ref(req_authn_context), "")

        user_id = processor.get_user_id(current_user)

        # Construct SamlResponse messages
        try:
            name_id_formats = self.IDP.config.getattr("name_id_format", "idp") or [NAMEID_FORMAT_UNSPECIFIED]
            name_id = NameID(format=name_id_formats[0], text=user_id)
            authn = AUTHN_BROKER.get_authn_by_accr(req_authn_context)
            sign_response = self.IDP.config.getattr("sign_response", "idp") or False
            sign_assertion = self.IDP.config.getattr("sign_assertion", "idp") or False
            authn_resp = self.IDP.create_authn_response(
                identity=identity,
                in_response_to="IdP_Initiated_Login",
                destination=destination,
                sp_entity_id=sp_entity_id,
                userid=user_id,
                name_id=name_id,
                authn=authn,
                sign_response=sign_response,
                sign_assertion=sign_assertion,
                **passed_data)
        except Exception as excp:
            return self.handle_error(exception=excp, status=500)

        # Return as html with self-submitting form.
        http_args = self.IDP.apply_binding(
            binding=binding_out,
            msg_str="%s" % authn_resp,
            destination=destination,
            relay_state=passed_data['RelayState'],
            response=True)
        return Response(http_args['data'])


class ProcessMultiFactorView(MethodView):
    """ This view is used in an optional step is to perform 'other' user validation, for example 2nd factor checks.
        Override this view per the documentation if using this functionality to plug in your custom validation logic.
    """
    decorators = [never_cache, login_required]

    def multifactor_is_valid(self, request):
        """ The code here can do whatever it needs to validate your user (via request.user or elsewise).
            It must return True for authentication to be considered a success.
        """
        return True

    def get(self):
        if self.multifactor_is_valid(request):
            logger.debug('MultiFactor succeeded for %s' % current_user)
            # TODO response

        logger.debug("MultiFactor failed; %s will not be able to log in" % current_user)
        logout_user()
        # TODO response
        return abort(401)


@never_cache
def metadata():
    """ Returns an XML with the SAML 2.0 metadata for this Idp.
        The metadata is constructed on-the-fly based on the config dict in the django settings.
    """
    conf = IdPConfig()
    conf.load(copy.deepcopy(current_app.config['SAML_IDP_CONFIG']))
    metadata = entity_descriptor(conf)
    return Response(response=str(metadata).encode('utf-8'), content_type="text/xml; charset=utf8")
