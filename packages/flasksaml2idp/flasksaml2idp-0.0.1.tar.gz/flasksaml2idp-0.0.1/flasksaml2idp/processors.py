from flask import current_app


class BaseProcessor:
    """ Processor class is used to determine if a user has access to a client service of this IDP
        and to construct the identity dictionary which is sent to the SP
    """

    def __init__(self, entity_id):
        self._entity_id = entity_id

    def has_access(self):
        """ Check if this user is allowed to use this IDP
        """
        return True

    def enable_multifactor(self, user):
        """ Check if this user should use a second authentication system
        """
        return False

    def get_user_id(self, user):
        """ Get identifier for a user. Take the one defined in settings.SAML_IDP_DJANGO_USERNAME_FIELD first, if not set
            use the USERNAME_FIELD property which is set on the user Model. This defaults to the user.username field.
        """
        # print(current_app.config)
        user_field = current_app.config['SAML_IDP_FLASK_USERNAME_FIELD'] \
            if 'SAML_IDP_FLASK_USERNAME_FIELD' in current_app.config else getattr(user, 'USERNAME_FIELD', 'username')
        return str(getattr(user, user_field))

    def create_identity(self, user, sp_mapping, **extra_config):
        """ Generate an identity dictionary of the user based on the given mapping of desired user attributes by the SP
        """

        return {
            out_attr: getattr(user, user_attr)
            for user_attr, out_attr in sp_mapping.items()
            if hasattr(user, user_attr)
        }
