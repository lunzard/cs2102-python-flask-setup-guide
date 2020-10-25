from flask_table import Table, Col, ButtonCol

class userInfoTable(Table):
    username = Col('Username ')
    contact = Col('Contact ')
    card = Col('Card ')
    usertype = Col('User Type ')
    postalcode = Col('Postal Code')

class editPetTable(Table):
    petname = Col('Pet Name ')
    pcontact = Col('Contact ')
    category = Col('Pet Name ')
    age = Col('Age ')
    edit = ButtonCol('Edit ', 'view.render_owner_pet_update', url_kwargs=dict(petname='petname', category='category', age='age'))
    delete = ButtonCol('Delete', 'view.render_owner_pet_delete', url_kwargs=dict(petname='petname'))

class ownerHomePage(Table):
    username = Col('Pet Name ')
    contact = Col('Contact ')
    postalcode = Col('Pet Name ')
    bid = ButtonCol('Bid', 'view.render_owner_bid_new', url_kwargs=dict(username='username', contact='contact', postalcode='postalcode', edit='contact'), url_kwargs_extra=dict(edit='edit'))