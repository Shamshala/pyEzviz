"""PyEzviz Exceptions."""

class PyEzvizError(Exception):
    """Ezviz api exception."""


class InvalidURL(PyEzvizError):
    """Invalid url exception."""


class HTTPError(PyEzvizError):
    """Invalid host exception."""


class InvalidHost(PyEzvizError):
    """Invalid host exception."""


class AuthTestResultFailed(PyEzvizError):
    """Authentication failed"""
