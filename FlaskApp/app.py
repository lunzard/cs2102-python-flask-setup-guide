import os
from flask import Flask

from __init__ import db, login_manager
from views import view

app = Flask(__name__)

# Routing
app.register_blueprint(view)


# Config
DATABASE_URL = os.environ['DATABASE_URL']

#app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://stiwcbueymtugr:37c18745f46467dbb42518378b2e794e8a5941d1febe535b3997daf14507e6cb@ec2-54-156-53-71.compute-1.amazonaws.com:5432/dekba31jf7kr6f?sslmode=require"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL+"?sslmode=require"
app.config["SECRET_KEY"] = "A random key to use flask extensions that require encryption"

# Initialize other components
db.init_app(app)
login_manager.init_app(app)


if __name__ == "__main__":
    app.run(
        debug=True,
        host="localhost",
        port=5000
    )
