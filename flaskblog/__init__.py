from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt # for password hashing
from flask_login import LoginManager # to manage logging in and out

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # to supress a warning
app.config['SECRET_KEY'] = 'cffcae1703372d4257eac8bca98ff7be'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app) 
 
login_manager = LoginManager(app) 
login_manager.login_view = 'login' # telling our login_manager where our login route is located
login_manager.login_message_category = 'info' # telling our login_manager where our login route is located


bcrypt = Bcrypt(app) # allows the bcrypt class to work on our app
from flaskblog import routes    