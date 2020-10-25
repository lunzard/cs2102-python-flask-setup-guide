from flask_table import Table, Col, ButtonCol

class userInfoTable(Table):
    username = Col('Username')
    contact = Col('Contact')
    card = Col('Card')
    usertype = Col('User Type')
    postalcode = Col('Postal Code')

class editPetTable(Table):
    petname = Col('Pet Name')
    pcontact = Col('Contact')
    category = Col('Pet Name')
    age = Col('Pet Name')
    edit = ButtonCol('Edit', 'view.render_owner_pet_update', url_kwargs=dict(petname='petname', category='category', age='age'))