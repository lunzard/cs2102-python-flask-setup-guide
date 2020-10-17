from flask_sqlalchemy import SQLAlchemy
##from sqlalchemy import create_engine
from flask_login import LoginManager

##engine = create_engine('postgres://rymjgqmiucferj:8e07c2a21509d15003f8cd12113219d602a59b1f6298da579e9e375b32da2c4c@ec2-3-231-16-122.compute-1.amazonaws.com:5432/df67v1kmbj2l9t?sslmode=disable')
db = SQLAlchemy()
login_manager = LoginManager()
