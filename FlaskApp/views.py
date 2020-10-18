from flask import Blueprint, redirect, flash, url_for, render_template
from flask_login import current_user, login_required, login_user, logout_user

from __init__ import db, login_manager
from forms import LoginForm, RegistrationForm
from models import Admins, PetOwners, CareTakers

view = Blueprint("view", __name__)


@login_manager.user_loader
def load_user(contact):
    contact = ((Admins.query.filter_by(contact=contact.data).first()) or
                (PetOwners.query.filter_by(contact=contact.data).first()) or
                (CareTakers.query.filter_by(contact=contact.data).first()))
    return contact or current_user


@view.route("/", methods=["GET"])
def render_dummy_page():
    return "<h1>Welcome to our CS2102 Project!</h1>\
    <h2>First time here? Click Register! If not, Login!</h2>"


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
        #query = "SELECT * FROM admins, petowners, caretakers WHERE contact = '{}'".format(contact)
        # exists_user = db.session.execute(query).fetchone()
        # if exists_user:
        #     form.username.errors.append("{} is already in use.".format(username))
        # else:
        if user_type == "admin":
            query = "INSERT INTO admins(username, contact, card, password) VALUES ('{}', '{}', '{}', '{}')"\
                .format(username, contact, credit_card, password)

            db.session.execute(query)
            db.session.commit()
        elif user_type == "petowner":
            query = "INSERT INTO petowners(username, contact, card, password) VALUES ('{}', '{}', '{}', '{}')"\
                .format(username, contact, credit_card, password)
            db.session.execute(query)
            db.session.commit()
        elif user_type == "caretaker":
            query = "INSERT INTO caretakers(username, contact, isPartTime, password) VALUES ('{}', '{}', '{}', '{}')"\
                .format(username, contact, is_part_time, password)
            db.session.execute(query)
            db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template("registration.html", title='Registration', form=form)


@view.route("/login", methods=["GET", "POST"])
def render_login_page():
    form = LoginForm()
    if form.is_submitted():
        print("username entered:", form.username.data)
        print("contact entered:", form.contact.data)
        print("password entered:", form.password.data)
    if form.validate_on_submit():
        contact = ((Admins.query.filter_by(contact=contact.data).first()) or
                   (PetOwners.query.filter_by(contact=contact.data).first()) or
                   (CareTakers.query.filter_by(contact=contact.data).first()))
        if contact:
            # TODO: You may want to verify if password is correct
            login_user(contact)
            return redirect("/privileged-page")
    return render_template("index.html", form=form)

@view.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('registration.html'))

@view.route("/privileged-page", methods=["GET"])
@login_required
def render_privileged_page():
    return "<h1>Hello, {}!</h1>".format(current_user.preferred_name or current_user.username)
