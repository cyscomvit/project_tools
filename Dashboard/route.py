from project_tools.Dashboard import app
from flask import render_template,redirect,url_for,flash,request,jsonify
from project_tools.Dashboard.models import Item,User
from project_tools.Dashboard.forms import RegistrationForm,LoginForm
from project_tools.Dashboard import db
from project_tools.tools.nmap.main import nmap_route
from flask_login import login_user
import json
#from project_tools.tools.JoomScan.passwordDictionary.endpoints import index2
from project_tools.tools.traceroute_flask.traceroute.endpoints import index3
from project_tools.tools.FlaskNikto.Nikto.endpoints import index4


def table(dic,stri):
    stri+="<table border='1'>\n"
    stri+="<colgroup>"
    stri+="<col style='background-color:#00CED1'>"
    stri+="<col style='background-color:#4CC417'>"
    stri+="</colgroup>\n"
    for keys in dic:
        stri+="<tr>\n"
        if type(dic[keys]) is dict:
            stri+="<td>"+keys+"</td>\n"
            stri+="<td>"+str(table(dic[keys],""))+"</td>\n"
        else:
            stri+="<td>"+keys+"</td>\n"
            if(type(dic[keys])!=str):
                dic[keys]=list(dic[keys])
            print(type(dic[keys]))
            stri+="<td>"+str(dic[keys])+"</td>\n"
        stri+="</tr>\n"
    stri+="</table>\n"
    return stri

    '''{% for keys in results %}
{%  if results.keys is mapping %}
<tr><td>{{   keys }}</td>
<td>{{ results.keys }}</td><tr>
{% else %}
<tr><td>{{ keys }} </td>
<td>{{ fun(results.keys,"") | safe }}</td></tr>
'''
@app.route('/')
@app.route('/home/') 
def home_page():
    return render_template('home.html')

@app.route('/dashboard',methods=['GET','POST'])
def dashboard_page():
    items=Item.query.all()
    result={}
    show=False
    if request.method=="POST":
        if request.form.get("nmap"):
            result = nmap_route()
            show=True  
            print(result)
        elif request.form.get("traceroute"):
            result = index3()
            show=True  
            print(result)
        elif request.form.get("nikto"):
            result = index4()
            show=True  
            if(result==None):
                result={"Status":"Success"}
            print(result)

    return render_template('dashboard.html',items=items,results=result,show=show,fun=table)

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

'''@app.route('/nmap',methods=['POST','GET'])
def nmapexec():
    print('called!')
    
    print(res)
    return redirect(url_for('dashboard_page',result=res))

@app.route('/Traceroute',methods=['POST', 'GET'])
def tr():
    print("called!")
    
    res = index3()
    print(res)
    return redirect(url_for('dashboard_page'))

@app.route('/Nikto',methods=['POST', 'GET'])
def nk():
    print("called!")
    
    res = index4()
    print(res)
    return redirect(url_for('dashboard_page'))'''