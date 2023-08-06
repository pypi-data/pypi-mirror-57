

class APIFailed(Exception):
    """
    Base Exception of firebase_api package.
    """
    ...


class NotFound(APIFailed):
    ...


class PermissionDenied(APIFailed):
    ...
