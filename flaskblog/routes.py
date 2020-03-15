from flask import render_template, url_for, flash, redirect
from flaskblog import app
from .forms import RegistrationForm, LoginForm
from .models import User, Post

posts = [
    {
        'author': 'Gregory Weiss',
        'title': 'Being a Genius For Dummies',
        'content': "I'm much smarter than you",
        'date_posted': 'March 15, 2020'
    },
    {
        'author': 'Jonathan Weiss',
        'title': 'Why am I so dumb?',
        'content': "Can you tie my shoes for me?  I can't figure it out",
        'date_posted': 'March 16, 2020'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for("home"))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
