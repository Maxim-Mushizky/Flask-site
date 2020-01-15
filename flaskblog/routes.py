from flask import render_template, url_for, flash, redirect
from flaskblog import app,db,bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Maxim Mushizky',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'December 16, 2019'
    },
    {
        'author': 'Robert Baratheon',
        'title': 'Blog post 2',
        'content': 'First stfu',
        'date_posted': 'December 02, 2019'

    }

]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', posts = posts, title = 'stfu_noob')

@app.route("/register", methods=['GET', 'POST']) #Accepts get and post requests in the registration form
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8') #hash the password
        # create new instance of User class:
        user = User(user_name = form.username.data, email = form.email.data, password = hashed_password )
        db.session.add(user) #add user to database
        db.session.commit() #commit- save it to db
        flash(f'Welcome {form.username.data}, Great success! You can now login into your new account', 'success') #show built in method flash in green
        return redirect(url_for('login')) #if validation is sucessful redirect to the home login
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)