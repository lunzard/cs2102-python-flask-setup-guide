from flask_table import Table, Col, ButtonCol

class userInfoTable(Table):
    username = Col('Username')
    contact = Col('Contact')
    card = Col('Card')
    usertype = Col('User Type')
    postalcode = Col('Postal Code')

class editPetTable(Table):
    petname = Col('Pet Name')
    contact = Col('pcontact')
    category = Col('Pet Name')
    age = Col('Pet Name')
    edit = ButtonCol('Edit', 'update', url_kwargs=dict(id='id')