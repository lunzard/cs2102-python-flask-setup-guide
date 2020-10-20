from __init__ import db, login_manager
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

@login_manager.user_loader
def load_user(contact):
    contact = ((Admins.query.filter_by(contact=contact).first()) or
                (Petowners.query.filter_by(contact=contact).first()) or
                (Caretakers.query.filter_by(contact=contact).first()))
    return contact


class Admins(db.Model, UserMixin):
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    contact = db.Column(db.String, primary_key=True)
    card = db.Column(db.String, nullable=True)
    usertype = db.Column(db.String, nullable=True)
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.contact

class Petowners(db.Model, UserMixin):
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    contact = db.Column(db.String, primary_key=True)
    card = db.Column(db.String, nullable=True)
    usertype = db.Column(db.String, nullable=True)
    pet = db.relationship('Pets', backref='owner')
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.contact
    
class Caretakers(db.Model, UserMixin):
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    contact = db.Column(db.String, primary_key=True)
    usertype = db.Column(db.String, nullable=True)
    isparttime = db.Column(db.Boolean, nullable=False)
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.contact
    
class Pets(db.Model, UserMixin):
    petname = db.Column(db.String, primary_key=True, nullable=False)
    pcontact = db.Column(db.String, db.ForeignKey('petowners.contact'), primary_key=True, nullable=False)
    category = db.Column(db.String, db.ForeignKey('categories.category'), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return (self.pcontact, self.petname)
    
class Available(db.Model, UserMixin):
    startdate = db.Column(db.Date, primary_key=True, nullable=False)
    enddate = db.Column(db.Date, primary_key=True, nullable=False)
    ccontact = db.Column(db.String, primary_key=True, nullable=False)
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return (self.startdate, self.enddate, self.ccontact)

class Biddings(db.Model, UserMixin):
    petname = db.Column(db.String, primary_key=True, nullable=False)
    pcontact = db.Column(db.String, primary_key=True, nullable=False)
    ccontact = db.Column(db.String, primary_key=True, nullable=False)
    startdate = db.Column(db.Date, primary_key=True, nullable=False)
    enddate = db.Column(db.Date, primary_key=True, nullable=False)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return (self.startdate, self.enddate, self.ccontact)
    