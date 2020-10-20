from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired, ValidationError, EqualTo
from models import Admins, Petowners, Caretakers

def is_valid_name(form, field):
    if not all(map(lambda char: char.isalpha(), field.data)):
        raise ValidationError('This field should only contain alphabets')

def is_valid_contact(self, contact):
        contact = ((Admins.query.filter_by(contact=contact.data).first()) or
                   (Petowners.query.filter_by(contact=contact.data).first()) or
                   (Caretakers.query.filter_by(contact=contact.data).first()))
        if contact:
            raise ValidationError('That contact is already being registered. Please choose a different one.')

# def is_valid_number(form, field):
#     if not all(map(lambda char: char.isnumber(), field.data)):
#         raise ValidationError('This field should only contain numbers')
    
# def is_valid_type(form, field):
#     if not all(map(lambda type: type == "pet owner" or type == "admin" or type == "caretaker", field.data)):
#         raise ValidationError('Please input valid user types such as pet owner, admin and caretaker')
    
def agrees_terms_and_conditions(form, field):
    if not field.data:
        raise ValidationError('You must agree to the terms and conditions to sign up')


class RegistrationForm(FlaskForm):
    username = StringField(
        label='Name',
        validators=[InputRequired(), is_valid_name],
        render_kw={'placeholder': 'Name', 'class': 'input100'}
    )
    usertype = StringField(
        label='Usertype',
        validators=[InputRequired()],
        render_kw={'placeholder': 'User Type', 'class': 'input100'}
    )
    contact = StringField(
        label='Contact',
        validators=[InputRequired(), is_valid_contact],
        render_kw={'placeholder': 'Contact', 'class': 'input100'}
    )
    password = PasswordField(
        label='Password',
        validators=[InputRequired()],
        render_kw={'placeholder': 'Password', 'class': 'input100'}
    )
    confirm_password = PasswordField(
        label='Confirm Password',
        validators=[InputRequired(), EqualTo('password')],
        render_kw={'placeholder': 'Confirmed Password', 'class': 'input100'}
    )
    credit_card = StringField(
        label='Credit Card',
        render_kw={'placeholder': 'Credit Card', 'class': 'input100'}
    )
    is_part_time = BooleanField(
        label='Is Part Time',
        render_kw={'placeholder': 'Is Part Time', 'class': 'input100'}
    )

class LoginForm(FlaskForm):
    contact = StringField(
        label='Contact',
        validators=[InputRequired()],
        render_kw={'placeholder': 'Contact', 'class': 'input100'}
    )
    password = PasswordField(
        label='Password',
        validators=[InputRequired()],
        render_kw={'placeholder': 'Password', 'class': 'input100'}
    )
    
class LoginForm(FlaskForm):
    pcontact = StringField(
    label='Contact',
    validators=[InputRequired()],
    render_kw={'placeholder': 'Contact', 'class': 'input100'}
    )
    password = PasswordField(
        label='Password',
        validators=[InputRequired()],
        render_kw={'placeholder': 'Password', 'class': 'input100'}
    )
    
    