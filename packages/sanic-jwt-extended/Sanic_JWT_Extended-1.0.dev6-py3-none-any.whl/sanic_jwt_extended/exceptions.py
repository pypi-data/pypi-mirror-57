class JWTExtendedException(Exception):
    """
    Base except which all sanic_jwt_extended errors extend
    """

    pass


class JWTDecodeError(JWTExtendedException):
    """
    An error decoding a JWT
    """

    pass


class InvalidHeaderError(JWTExtendedException):
    """
    An error getting header information from a request
    """

    pass


class NoAuthorizationError(JWTExtendedException):
    """
    An error raised when no authorization token was found in a protected endpoint
    """

    pass


class WrongTokenError(JWTExtendedException):
    """
    Error raised when attempting to use a refresh token to access an endpoint
    or vice versa
    """

    pass


class RevokedTokenError(JWTExtendedException):
    """
    Error raised when a revoked token attempt to access a protected endpoint
    """

    pass


class FreshTokenRequiredError(JWTExtendedException):
    """
    Error raised when a valid, non-fresh JWT attempt to access an endpoint
    protected by jwt_required with fresh_required is True
    """

    pass


class AccessDeniedError(JWTExtendedException):
    """
    Error raised when a valid JWT attempt to access an endpoint
    protected by jwt_required with not allowed role
    """

    pass


class ConfigurationConflictError(JWTExtendedException):
    """
    Error raised when trying to use allow and deny option together in jwt_required
    """

    pass


class CSRFError(JWTExtendedException):
    pass
