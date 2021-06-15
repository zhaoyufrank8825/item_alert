class UserError(Exception):
    def __init__(self, msg):
        self.msg = msg

class UserNotFoundError(UserError):
    pass

class UserAlreadyRegisteredError(UserError):
    pass

class InvalidEmailError(UserError):
    pass

class PasswordDonotMatchError(UserError):
    pass

class IncorrectPasswordError(UserError):
    pass
