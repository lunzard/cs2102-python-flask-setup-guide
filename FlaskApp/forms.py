from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, BooleanField
from wtforms.validators import InputRequired, ValidationError, EqualTo
from FlaskApp.models import Admin, PetOwner, CareTaker

def is_valid_name(form, field):
    if not all(map(lambda char: char.isalpha(), field.data)):
        raise ValidationError('This field should only contain alphabets')

def is_valid_contact(self, contact):
        contact = ((Admin.query.filter_by(contact=contact.data).first()) or
                   (PetOwner.query.filter_by(contact=contact.data).first()) or
                   (CareTaker.query.filter_by(contact=contact.data).first()))
        if contact:
            raise ValidationError('That contact is already being registered. Please choose a different one.')

# def is_valid_number(form, field):
#     if not all(map(lambda char: char.isnumber(), field.data)):
#         raise ValidationError('This field should only contain numbers')
    
def is_valid_type(form, field):
    if not all(map(lambda type: type in {"pet owner", "admin", "caretaker"}, field.data)):
        raise ValidationError('Please input valid user types such as pet owner, admin and caretaker')
    
def agrees_terms_and_conditions(form, field):
    if not field.data:
        raise ValidationError('You must agree to the terms and conditions to sign up')


class RegistrationForm(FlaskForm):
    username = StringField(
        label='Name',
        validators=[InputRequired(), is_valid_name],
        render_kw={'placeholder': 'Name'}
    )
    user_type = StringField(
        label='User Type',
        validators=[InputRequired(), is_valid_type],
        render_kw={'placeholder': 'User Type'}
    )
    contact = IntegerField(
        label='Contact',
        validators=[InputRequired(), is_valid_contact],
        render_kw={'placeholder': 'Contact'}
    )
    password = PasswordField(
        label='Password',
        validators=[InputRequired()],
        render_kw={'placeholder': 'Password'}
    )
    confirm_password = PasswordField(
        label='Confirm Password',
        validators=[InputRequired(), EqualTo('password')],
        render_kw={'placeholder': 'Confirmed Password'}
    )
    credit_card = IntegerField(
        label='Credit Card',
        render_kw={'placeholder': 'Credit Card'}
    )
    is_part_time = BooleanField(
        label='Is Part Time',
        render_kw={'placeholder': 'Is Part Time'}
    )
    # submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField(
        label='Name',
        validators=[InputRequired()],
        render_kw={'placeholder': 'Name', 'class': 'input100'}
    )
    contact = IntegerField(
        label='Contact',
        validators=[InputRequired()],
        render_kw={'placeholder': 'Contact', 'class': 'input100'}
    )
    password = PasswordField(
        label='Password',
        validators=[InputRequired()],
        render_kw={'placeholder': 'Password', 'class': 'input100'}
    )
    # submit = SubmitField('Login')