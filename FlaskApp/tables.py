from flask_table import Table, Col

class userInfoTable(Table):
    username = Col('Username')
    contact = Col('Contact')
    card = Col('Card')
    usertype = Col('User Type')
    postalcode = Col('Postal Code')

