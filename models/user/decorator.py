from typing import Callable
import functools
from flask import session, flash, url_for, redirect, current_app


def require_login(f: Callable):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('email'):
            flash("You need to be signed in for this page.", "danger")
            return redirect(url_for("users.login"))
        return f(*args, **kwargs)
    return decorated_function

def require_admin(f: Callable):
    @functools.wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('email') == current_app.config.get("ADMIN", ""):
            flash("You need to be the administrator to access this page.", "danger")
            return redirect(url_for("users.login"))
        return f(*args, **kwargs)
    return decorated_function

