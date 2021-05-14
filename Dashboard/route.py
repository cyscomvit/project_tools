from Dashboard import app
from flask import render_template,redirect,url_for,flash
from Dashboard.models import Item,User
from Dashboard.forms import RegistrationForm,LoginForm
from Dashboard import db
from flask_login import login_user
@app.route('/')
@app.route('/home/') 
def home_page():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard_page():
    items=Item.query.all()
    return render_template('dashboard.html',items=items)

@app.route('/register',methods=['GET','POST'])
def register_page():
    form= RegistrationForm()
    if form.validate_on_submit():
        user_to_create =User(username=form.username.data,email_address=form.email.data,password=form.password1.data)
        
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('dashboard_page'))
    
    if form.errors !={}: 
        for e in form.errors.values():
            flash(f'Error! {e}',category='danger')


    return render_template('register.html',form = form)

@app.route('/login',methods=['GET','POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
    #     attempted_password= User.query.filter_by(password=form.password.data).first()
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password= form.password.data):
            login_user(attempted_user)
            flash('Success',category='success')
            return redirect(url_for('dashboard_page'))
        else:
            flash('failed',category='danger')


               
    return render_template('login.html',form=form)

