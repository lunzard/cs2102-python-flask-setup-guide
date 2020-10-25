from flask_table import Table, Col

class userInfoTable(Table):
    username = Col('Username')
    contact = Col('Contact')
    card = Col('Card')
    password = Col('Password')
    usertype = Col('User Type')
    isparttime = Col('Part Time?')
    postalcode = Col('Postal Code')

