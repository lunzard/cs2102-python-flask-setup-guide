from flask_table import Table, Col

class userInfoTable(Table):
    username = Col('Username')
    contact = Col('Contact')
    usertype = Col('User Type')
    card = Col('Card')
    postalcode = Col('Postal Code')

