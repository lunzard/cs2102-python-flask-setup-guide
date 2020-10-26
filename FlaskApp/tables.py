from flask_table import Table, Col, ButtonCol, LinkCol

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

class editAvailableTable(Table):
    startdate = Col('Start Date ')
    enddate = Col('End Date ')
    ccontact = Col('Contact')
    edit = ButtonCol('Edit ', 'view.render_caretaker_available_edit', url_kwargs=dict(startdate='startdate', enddate='enddate'))
    delete = ButtonCol('Delete', 'view.render_caretaker_available_delete', url_kwargs=dict(startdate='startdate', enddate='enddate'))

class ownerHomePage(Table):
    username = Col('Caretaker Name ')
    contact = Col('Contact ')
    postalcode = Col('Postal Code ')
    bid = LinkCol('Bid', 'view.render_owner_bid_new', url_kwargs=dict(username='username', ccontact='contact', postalcode='postalcode', edit='contact'), url_kwargs_extra=dict(edit='edit'))


class bidding(Table):
    pcontact = ('Owner Contact')	
    ccontact = ('Caretaker Contact')	
    petname	= ('Pet name')
    startdate = ('Start date')
    enddate = ('End date')
    paymentmode = ('Payment mode')
    deliverymode = ('Delivery mode')
    status = ('Status')

class biddingCaretakerTable(Table):
    pcontact = ('Owner Contact')	
    ccontact = ('Caretaker Contact')	
    petname	= ('Pet name')
    startdate = ('Start date')
    enddate = ('End date')
    paymentmode = ('Payment mode')
    deliverymode = ('Delivery mode')
    status = ('Status')
    accept = LinkCol('Accept', 'view.render_caretaker_biddings_accept', url_kwargs=dict(ownerContact='pcontact', 
        ccontact='ccontact', petName='petname', startDay='startdate', endDay='enddate'))
