from application import app
from flask import render_template, flash, redirect, url_for, request
from application.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            flash("Login Successful")
            return redirect('/index')
    else:
        return render_template(
            'login.html',
            title='Login to Action-Central',
            form=form)