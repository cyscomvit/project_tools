from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Dashboard.db'    
app.config['SECRET_KEY']='shiv_nuemen'
db=SQLAlchemy(app)         


bcrypt= Bcrypt(app)
login_manager= LoginManager(app)
from Dashboard import route

