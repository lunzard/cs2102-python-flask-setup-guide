from flask import Blueprint, redirect, flash, url_for, render_template, request
from flask_login import current_user, login_required, login_user, logout_user
from flask_user import roles_required
from __init__ import db, login_manager, bcrypt
from forms import LoginForm, RegistrationForm, BiddingForm, PetForm
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
        postal_code = form.postal_code.data
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        query = "INSERT INTO users(username, contact, card, password, usertype, isPartTime, postalcode) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')" \
            .format(username, contact, credit_card, hashed_password, user_type, is_part_time, postal_code)
        db.session.execute(query)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect("/login")
    return render_template("registration.html", title='Registration', form=form)


@view.route("/login", methods=["GET", "POST"])
def render_login_page():
    if current_user.is_authenticated:
        next_page = request.args.get('next')
        if next_page:
            print("nextpage", flush=True)
            return redirect(next_page)
        elif current_user.usertype == "admin":
            print("admin", flush=True)
            return redirect("/admin")
        elif current_user.usertype == "petowner":
            print("current", flush=True)
            return redirect("/owner")
        elif current_user.usertype == "caretaker":
            print("caret", flush=True)
            return redirect("/caretaker")
        else:
            print("nothing mtaches", flush=True)
            return redirect("/profile")
    form = LoginForm()
    if form.validate_on_submit():
        print("submited", flush=True)
        user = ((Admins.query.filter_by(contact=form.contact.data).first()) or
                (Petowners.query.filter_by(contact=form.contact.data).first()) or
                (Caretakers.query.filter_by(contact=form.contact.data).first()))
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            print("found", flush=True)
            login_user(user, remember=True)
            next_page = request.args.get('next')
            if next_page:
                print("nextpage", flush=True)
                return redirect(next_page)
            elif current_user.usertype == "admin":
                print("admin", flush=True)
                return redirect("/admin")
            elif current_user.usertype == "petowner":
                print("current", flush=True)
                return redirect("/owner")
            elif current_user.usertype == "caretaker":
                print("caret", flush=True)
                return redirect("/caretaker")
            else:
                print("nothing matches", flush=True)
                return redirect("/profile")
        else:
            print("not found", flush=False)
            flash('Login unsuccessful. Please check your contact and password', 'danger')
    return render_template("realLogin.html", form=form)


@view.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect("/")


# ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN ADMIN


@view.route("/admin", methods=["GET"])
@login_required
def render_admin_page():
    print(current_user, flush=True)
    contact = current_user.contact
    query = "SELECT * FROM admins WHERE contact = '{}'".format(contact)
    results = db.session.execute(query).fetchall()
    return render_template('admin.html', results=results, username=current_user.username + " admin")


@view.route("/admin/summary", methods=["GET"])
@login_required
def render_admin_summary_page():
    query = "SELECT * FROM caretakers"
    results = db.session.execute(query).fetchall()
    return render_template("profile.html", results=results, username=current_user.username + " owner")

@view.route("/caretaker", methods=["GET"])
@login_required
def render_caretaker_page():
    return render_template('profile.html', username=current_user.username + " caretaker")


@view.route("/caretaker/biddings", methods=["GET", "POST"])
@login_required
def render_caretaker_biddings():
    form = BiddingForm()
    contact = current_user.contact
    query = "SELECT * FROM biddings WHERE contact = '{}'".format(contact)
    results = db.session.execute(query).fetchall()
    return render_template("profile.html", results=results, username=current_user.username + " owner")


@view.route("/caretaker/profile", methods=["GET"])
@login_required
def render_caretaker_profile():
    return render_template('profile.html', username=current_user.username + " caretaker")


@view.route("/caretaker/update-profile", methods=["GET"])
@login_required
def render_caretaker_update_profile():
    return render_template('profile.html', username=current_user.username + " caretaker")


@view.route("/caretaker/available", methods=["GET", "POST"])
@login_required
def render_caretaker_available():
    return render_template('profile.html', username=current_user.username + " caretaker")


@view.route("/caretaker/available/edit", methods=["GET", "POST"])
@login_required
def render_caretaker_available_edit():
    return render_template('profile.html', username=current_user.username + " caretaker")


@view.route("/caretaker/available/delete", methods=["GET", "POST"])
@login_required
def render_caretaker_available_delete():
    return render_template('profile.html', username=current_user.username + " caretaker")


@view.route("/caretaker/available/new", methods=["GET", "POST"])
@login_required
def render_caretaker_available_new():
    return render_template('profile.html', username=current_user.username + " caretaker")


@view.route("/caretaker/update-cantakecare", methods=["GET", "POST"])
@login_required
def render_caretaker_update_cantakecare():
    return render_template('profile.html', username=current_user.username + " caretaker")


# END OF CARETAKER END OF CARETAKER END OF CARETAKER END OF CARETAKER END OF CARETAKER END OF CARETAKER

# PETOWNER PETOWNER PETOWNER PETOWNER PETOWNER PETOWNER PETOWNER PETOWNER PETOWNER PETOWNER PETOWNER


@view.route("/owner", methods=["GET", "POST"])
@login_required
def render_owner_page():
    query = "SELECT * FROM caretakers"
    results = db.session.execute(query).fetchall()
    return render_template("owner.html", results=results, username=current_user.username + " owner")


@view.route("/owner/summary", methods=["GET", "POST"])
@login_required
def render_owner_summary():
    contact = current_user.contact
    query = "SELECT * FROM petowners WHERE contact = '{}'".format(contact)
    results = db.session.execute(query).fetchall()
    return render_template("profile.html", results=results, username=current_user.username + " owner")


@view.route("/owner/profile", methods=["GET", "POST"])
@login_required
def render_owner_profile():
    query = "SELECT * FROM caretakers"
    results = db.session.execute(query).fetchall()
    return render_template("profile.html", results=results, username=current_user.username + " owner")


@view.route("/owner/profile/update", methods=["GET", "POST"])
@login_required
def render_owner_profile_update():
    query = "SELECT * FROM caretakers"
    results = db.session.execute(query).fetchall()
    return render_template("profile.html", results=results, username=current_user.username + " owner")


@view.route("/owner/pet", methods=["GET", "POST"])
@login_required
def render_owner_pet():
    contact = current_user.contact
    query = "SELECT * FROM pets WHERE pcontact = '{}'".format(contact)
    results = db.session.execute(query).fetchall()
    return render_template("profile.html", results=results, username=current_user.username + " owner")


@view.route("/owner/pet/new", methods=["GET", "POST"])
@login_required
def render_owner_pet_new():
    form = PetForm()
    if request.method == 'POST' and form.validate_on_submit():
        return redirect(url_for(render_owner_pet))
    contact = current_user.contact
    return render_template("profile.html", form=form, username=current_user.username + " owner")


@view.route("/owner/pet/update", methods=["POST"])
@login_required
def render_owner_pet_update():
    return redirect(url_for(render_owner_pet))


@view.route("/owner/pet/delete", methods=["POST"])
@login_required
def render_owner_pet_delete():
    query = "SELECT * FROM caretakers"
    results = db.session.execute(query)
    return redirect(url_for(render_owner_pet))


@view.route("/owner/bid", methods=["GET", "POST"])
@login_required
def render_owner_bid():
    form = BiddingForm()
    
    contact = current_user.contact
    query = "SELECT * FROM biddings WHERE pcontact = '{}'".format(contact)
    results = db.session.execute(query)
    return render_template("profile.html", form=form, results=results, username=current_user.username + " owner")


@view.route("/owner/bid/new", methods=["GET", "POST"])
@login_required
def render_owner_bid_new():
    form = BiddingForm()
    if request.method == 'POST' and form.validate_on_submit():
        redirect(url_for(render_owner_bid))
    return render_template("profile.html", form=form, username=current_user.username + " owner")


@view.route("/owner/bid/update", methods=["GET", "POST"])
@login_required
def render_owner_bid_update():
    query = "SELECT * FROM caretakers"
    results = db.session.execute(query)
    return render_template("profile.html", results=results, username=current_user.username + " owner")


@view.route("/owner/bid/delete", methods=["GET", "POST"])
@login_required
def render_owner_bid_delete():
    query = "SELECT * FROM caretakers"
    results = db.session.execute(query)
    return render_template("profile.html", results=results, username=current_user.username + " owner")


# END OF PETOWNER END OF PETOWNER END OF PETOWNER END OF PETOWNER END OF PETOWNER END OF PETOWNER END OF PETOWNER


@view.route("/profile")
@login_required
def render_profile_page():
    return render_template('profile.html', username=current_user.username + "profile")


@view.route('/update/username', methods=['POST', 'GET'])
@login_required
def update(contact):
    user_to_update = Admins.query.get_or_404(contact)
    if request.method == "POST" and form.validate_on_submit():
        user_to_update.username = request.form['username']
        try:
            db.session.commit()
            return redirect('/profile')
        except:
            return "There is a problem updating user"
    else:
        return render_template('update.html', user_to_update=user_to_update)
