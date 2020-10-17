from flask import Flask

from __init__ import db, login_manager
from views import view

app = Flask(__name__)

# Routing
app.register_blueprint(view)


# Config
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://rymjgqmiucferj:8e07c2a21509d15003f8cd12113219d602a59b1f6298da579e9e375b32da2c4c@ec2-3-231-16-122.compute-1.amazonaws.com:5432/df67v1kmbj2l9t?sslmode=require"
app.config["SECRET_KEY"] = "A random key to use flask extensions that require encryption"

# Initialize other components
db.init_app(app)
db.session.execute("DROP TABLE petowners")
db.session.execute("CREATE TABLE petowners(username VARCHAR PRIMARY KEY NOT NULL)")
login_manager.init_app(app)


if __name__ == "__main__":
    app.run(
        debug=True,
        host="localhost",
        port=5000
    )
