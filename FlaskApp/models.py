from __init__ import db, login_manager
from flask_login import UserMixin

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
    isparttime = db.Column(db.Boolean, nullable=False)
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.contact