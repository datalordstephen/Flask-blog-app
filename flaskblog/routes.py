from flask import render_template, url_for, flash, redirect , request
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

from flaskblog import app, db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required

posts = [
    {
        'author' : 'Malik Chupapi',
        'title' : 'RAIN and it\'s hazards',
        'content' : 'RAIN has a lot of hazards',
        'date_posted' : 'March 20, 2019'
    },
     {
        'author' : 'Tife Odegaard',
        'title' : 'RAIN and it\'s pluses',
        'content' : 'RAIN has a lot of pluses',
        'date_posted' : 'June 14, 2017'
    }
]

@app.route('/') 
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title= 'About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You can now proceed to log in', 'success')
        return redirect(url_for('login')) #redirects to the login page upon successful creation of account
    return render_template('register.html', title = 'Register', form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data) # logs in the user
            next_page = request.args.get('next')
            print(next_page)
            flash(f"Welcome back, {user.username}!", 'success')
            # redirects us to the set next page or the home page
            return redirect(next_page) if next_page else redirect(url_for('home')) 
        else: 
            flash("Login Failed, Check your details and try again", 'danger')
    return render_template('login.html', title = 'Login', form = form)

@app.route('/logout')
def logout():
    logout_user() 
    return redirect(url_for('home')) # redirects to the home page

@app.route('/account')
@login_required # makes our app require a user to be logged in before allowing access to this route
def account():
    return render_template('account.html', title = 'Account')
