from datetime import datetime
from flaskblog import db, login_manager

from flask_login import UserMixin

# a decorated function for reloading the user from the user_id stored in the session 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin): # inheriting from the UserMixin as well
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True,  nullable = False)
    email = db.Column(db.String(120), unique = True, nullable  = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable  = False)
    # since users are related to their posts, a relationship is defined
    posts = db.relationship('Post', backref='author', lazy=True) #creates a "column" in the posts table that connects every post to the user who wrote it
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default= datetime.utcnow) 
    post_content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False) #referencing the id of the user that writes a post as a foreign key
    
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"