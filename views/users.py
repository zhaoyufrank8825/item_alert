from flask import Blueprint, flash, request, render_template, session, redirect, url_for
from models.user import User, UserErrors
# import models.user.errors as UserErrors


user_blueprint = Blueprint("users", __name__)


@user_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        password2 = request.form['password2']
        username = request.form['username']

        if password == password2:
            try:
                User.register(email, password, username)
                session['email']=email
                return render_template("alerts/index.html")
            except UserErrors.UserError as e:
                return e.msg
        else:
            flash("The confirmed password doesn't match with password.", "danger")
            return render_template("users/register.html")
            # raise UserErrors.PasswordDonotMatchError("The confirmed password doesn't match with password.")
    return render_template("users/register.html")


@user_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        try:
            if User.is_login_valid(email, password):
                session['email']=email
                return redirect(url_for("stores.index"))
        except UserErrors.UserError as e:
            return e.msg
        
    return render_template("users/login.html")

@user_blueprint.route("/logout")
def logout():
    session['email'] = None
    return redirect(url_for(".login"))
