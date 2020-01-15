from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] =  'a450b94e87f74f4b4a36b435f38c51c1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #specify relative path to db. ///is relative to the the file where call is made
db = SQLAlchemy(app) #create SQLAlchemy database instances
bcrypt = Bcrypt(app) #init Bcrypt class with app instance of Flask class
login_manager = LoginManager(app)


from flaskblog import routes