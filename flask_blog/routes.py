from flask import render_template, flash, redirect, url_for
from flask_blog.forms import RegistrationForm, LoginForm
from flask_blog.models import Users, Post
from flask_blog import app


posts = [
    {
        "id": '01',
        "author":  "Ayush Chauhan",
        "title": "Test Post_1 ",
        "description": "Blog Post One Description",
        "ImageUrl": "None"
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
        flash(f'Account created for {form.username.name}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)