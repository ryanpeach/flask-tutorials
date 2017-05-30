from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Ryan'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

# index view function suppressed for brevity

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('slogin.html', 
                           title='Sign In')
