from flaskblog import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) #get the user by the user_id

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True) #id col will be primary key for User tabel
    user_name = db.Column(db.String(20), unique = True, nullable = False) #VARCHAR(20), has to be unique and non nullable
    email = db.Column(db.String(120), unique=True, nullable=False)  # VARCHAR(120), has to be unique and non nullable
    image_file = db.Column(db.String(20), unique=False, nullable=False, default = 'default.jpg') #Create default.jpg user image
    password = db.Column(db.String(60), nullable = False)
    posts =  db.relationship('Post', backref='author', lazy=True) #refering to Post class. backref gives all the User detail who created a post

    def __repr__(self):
        return f"user('{self.user_name}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.utcnow) #date posted- DateTime variable with default of current time
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False) #we are refering to user table and id column

    def __repr__(self):
        return f"user('{self.title}', '{self.date_posted}')"
