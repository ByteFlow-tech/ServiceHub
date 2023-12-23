class AuthException(Exception):
    message: str


class Stop(Exception):
    pass