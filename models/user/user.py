from models.blog import Blog
import uuid
from flask import flash, redirect, url_for, render_template
from dataclasses import dataclass, field
from common.utils import Utils
import models.user.errors as UserErrors
from models.model import Model


@dataclass
class User(Model):
    collection: str = field(init=False, default="users")
    email: str
    password: str
    username: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    def json(self):
        return {
            "email": self.email,
            "password": self.password,
            "_id": self._id,
            "username": self.username
        }
    
    @classmethod
    def find_by_email(cls, email):
        try:
            return cls.find_one_by("email", email)
        except TypeError:
            # flash("A user with this email was not found.", "danger")
            # return render_template("users/register.html")
            raise UserErrors.UserNotFoundError("A user with this email was not found.")

    @classmethod
    def register(cls, email, password, username):
        if not Utils.email_valid(email):
            flash("The email does not have the righ format.", "danger")
            return render_template("users/register.html")
            # raise UserErrors.InvalidEmailError("The email does not have the righ format.")
        
        try:
            cls.find_by_email(email)
            flash("The email you used to register already exists.", "danger")
            return render_template("users/register.html")
            # raise UserErrors.UserAlreadyRegisteredError("The email you used to register already exists.")
        except UserErrors.UserNotFoundError:
            flash("Create new user.", "danger")
            User(email, Utils.hash_password(password), username).save_to_mongo()

    @classmethod
    def is_login_valid(cls, email, password):
        user = User.find_by_email(email)

        if not Utils.check_hashed_password(password, user.password):
            flash("The password was incorrect.", "danger")
            return render_template("users/login.html")
            # raise UserErrors.IncorrectPasswordError("The password was incorrect.")
        return True

    def get_blogs(self):
        return Blog.find_by_author_id(self._id)

    def new_blog(self, title, description):
        blog = Blog(self.email, title, description, self._id)
        blog.save_to_mongo()

    @staticmethod
    def new_post(blog_id, title, content):
        blog = Blog.from_mongo(blog_id)
        blog.new_post(title, content)
    
    @classmethod
    def get_by_email(cls, email):
        return cls.find_one_by("email", email)
        
