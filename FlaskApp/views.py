from flask import Blueprint, redirect, flash, url_for, render_template, request
from flask_login import current_user, login_required, login_user, logout_user
from __init__ import db, login_manager, bcrypt
from forms import LoginForm, RegistrationForm
from models import Admins, Petowners, Caretakers
import sys

view = Blueprint("view", __name__)


# @login_manager.user_loader
# def load_user(contact):
#     contact = ((Admins.query.filter_by(contact=contact.data).first()) or
#                 (Petowners.query.filter_by(contact=contact.data).first()) or
#                 (Caretakers.query.filter_by(contact=contact.data).first()))
#     return current_user or contact


@view.route("/", methods=["GET"])
def render_dummy_page():
    return render_template("welcome.html", title='Welcome')


@view.route("/registration", methods=["GET", "POST"])
def render_registration_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user_type = form.usertype.data
        contact = form.contact.data
        credit_card = form.credit_card.data
        is_part_time = form.is_part_time.data
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        if user_type == "admin":
            query = "INSERT INTO admins(username, contact, card, password) VALUES ('{}', '{}', '{}', '{}')"\
                .format(username, contact, credit_card, hashed_password)
            db.session.execute(query)
            db.session.commit()
        elif user_type == "petowner":
            query = "INSERT INTO petowners(username, contact, card, password) VALUES ('{}', '{}', '{}', '{}')"\
                .format(username, contact, credit_card, hashed_password)
            db.session.execute(query)
            db.session.commit()
        elif user_type == "caretaker":
            query = "INSERT INTO caretakers(username, contact, isPartTime, password) VALUES ('{}', '{}', '{}', '{}')"\
                .format(username, contact, is_part_time, hashed_password)
            db.session.execute(query)
            db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect("/login")
    return render_template("registration.html", title='Registration', form=form)


@view.route("/login", methods=["GET", "POST"])
def render_login_page():
    if current_user.is_authenticated:
        if next_page:
            return redirect(next_page)
        elif current_user.user_type == "admin": 
            redirect("/admin")
        elif current_user.user_type == "owner": 
            redirect("/owner")
        elif current_user.user_type == "caretaker": 
            redirect("/caretaker")
        else:
            redirect("/profile")
    form = LoginForm()
    if form.validate_on_submit():
        print("submited", flush=True)
        user = ((Admins.query.filter_by(contact=form.contact.data).first()) or
                (Petowners.query.filter_by(contact=form.contact.data).first()) or
                (Caretakers.query.filter_by(contact=form.contact.data).first()))
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            print("found", flush=True)
            login_user(user)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            elif current_user.user_type == "admin": 
                redirect("/admin")
            elif current_user.user_type == "owner": 
                redirect("/owner")
            elif current_user.user_type == "caretaker": 
                redirect("/caretaker")
            else:
                redirect("/profile")
        else:
            print("not found", flush=False)
            flash('Login unsuccessful. Please check your contact and password', 'danger')
    return render_template("realLogin.html", form=form)

@view.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@view.route("/admin", methods=["GET"])
@login_required
def render_admin_page():
    return "<h1>Hello, {}! You are an admin. </h1>".format(current_user.username)

@view.route("/owner", methods=["GET"])
@login_required
def render_owner_page():
    return "<h1>Hello, {}! You are a pet owner. </h1>".format(current_user.username)

@view.route("/caretaker", methods=["GET"])
@login_required
def render_caretaker_page():
    return "<h1>Hello, {}! You are a caretaker.</h1>".format(current_user.username)



@view.route("/profile")
@login_required
def render_profile_page():
    return render_template("profile.html")