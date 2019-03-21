from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__, static_folder="static")
app.config['SECRET_KEY'] = '6dc254fb4f3d47651181357302507fa3777e00e8a82b26dc'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://c1815697:aBegJj3dDCChbDC@csmysql.cs.cf.ac.uk:3306/c1815697'

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from shop import routes
