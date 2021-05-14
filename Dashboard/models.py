from enum import unique
from sqlalchemy.orm import backref
from Dashboard import db
from Dashboard import bcrypt,login_manager
from flask_login import UserMixin

@login_manager.user_loader  
def load_user(user_id):
    return User.query.get(int(user_id)) 

class User(db.Model, UserMixin):
    id= db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(length=30),nullable = False, unique=True)
    email_address = db.Column(db.String(length=50),nullable= False,unique=True)
    password_hash = db.Column(db.String(length=60),nullable= False,unique=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self,plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')
    
    def check_password_correction(self,attempted_password):
       return bcrypt.check_password_hash(self.password_hash,attempted_password)
           

class Item(db.Model): 
    id=db.Column(db.Integer(),primary_key=True)
    name= db.Column(db.String(length=30),nullable=False, unique=True)
    description = db.Column(db.String(length=2048),nullable=False,unique=True)
    
    
    
    def __repr__(self):
        return f'Item {self.name}'





    
    
