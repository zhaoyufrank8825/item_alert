import re
from passlib.hash import pbkdf2_sha512


class Utils:
    @staticmethod
    def email_valid(email):
        pattern = re.compile(r"^[\w-]+@([\w-]+\.)+[\w]+$")
        return True if pattern.match(email) else False

    @staticmethod
    def hash_password(password):
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        return pbkdf2_sha512.verify(password, hashed_password)

