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
    biddingccontact = db.relationship('Biddings', backref='contact')
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
    biddingpetname = db.relationship('Biddings', backref='pet')
    biddingpcontact = db.relationship('Biddings', backref='contact', primaryjoin="Pets.pcontact==Biddings.pcontact")
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
    
    def get_key(self):
        return (self.startdate, self.enddate, self.ccontact)

class Biddings(db.Model, UserMixin):
    petname = db.Column(db.String, db.ForeignKey('pets.petname'), primary_key=True, nullable=False)
    pcontact = db.Column(db.String, db.ForeignKey('pets.pcontact'), primary_key=True, nullable=False)
    ccontact = db.Column(db.String, db.ForeignKey('caretakers.contact'), primary_key=True, nullable=False)
    startdate = db.Column(db.Date, primary_key=True, nullable=False)
    enddate = db.Column(db.Date, primary_key=True, nullable=False)
    paymentmode = db.Column(db.String, nullable=False)
    deliverymode = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)
    
    reviewpetname = db.relationship('Reviews', backref='pet')
    reviewpcontact = db.relationship('Reviews', backref='petonwercontact')
    reviewccontact = db.relationship('Reviews', backref='caretakercontact')
    reviewstartdate = db.relationship('Reviews', backref='start')
    reviewenddate = db.relationship('Reviews', backref='end')
    
    def get_status(self):
        return self.status

    def get_key(self):
        return (self.startdate, self.enddate, self.ccontact, self.petname, self.pcontact)
    
class Reviews(db.Model, UserMixin):
    petname = db.Column(db.String, db.ForeignKey('biddings.petname'), primary_key=True, nullable=False)
    pcontact = db.Column(db.String, db.ForeignKey('biddings.pcontact'), primary_key=True, nullable=False)
    ccontact = db.Column(db.String, db.ForeignKey('biddings.ccontact'), primary_key=True, nullable=False)
    startdate = db.Column(db.Date, db.ForeignKey('biddings.startdate'), primary_key=True, nullable=False)
    enddate = db.Column(db.Date, db.ForeignKey('biddings.enddate'), primary_key=True, nullable=False)
    rating = db.Column(db.Integer, primary_key=True, nullable=False)
    review = db.Column(db.String, primary_key=True, nullable=False)
    
    def get_rating(self):
        return self.rating
 
    def get_key(self):
        return (self.startdate, self.enddate, self.ccontact, self.petname, self.pcontact, self.rating, self.review)
    
    