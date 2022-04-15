from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Email, Length, DataRequired, EqualTo, ValidationError #Validators for the different fields

# importing our User model in order to validate if a username or email already exists 
from flaskblog.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                        validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                        validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', 
                        validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # function to validate the username 
    def validate_username(self, username):
        candidate = User.query.filter_by(username = username.data).first()
        if candidate: #if the username exists
            raise ValidationError('This username is taken -_-')
    
    # function to validate the email 
    def validate_email(self, email):
        candidate = User.query.filter_by(email = email.data).first()
        if candidate: #if the email exists
            raise ValidationError('This email is taken -_-')

class LoginForm(FlaskForm):
    email = StringField('Email', 
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', 
                        validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')