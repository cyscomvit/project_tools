from wtforms.fields.simple import PasswordField
from wtforms import validators
from flask_wtf import FlaskForm
from Dashboard.models import User
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,EqualTo,Email,DataRequired, ValidationError

class RegistrationForm(FlaskForm):
    def validate_username(self,username_to_check):
        user=User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists')
    
    def validate_email(self,email_to_check):
        email_address=User.query.filter_by(email_address=email_to_check.data).first()
        if email_address:
            raise ValidationError('email address already exists')



    username = StringField(label='User Name',validators=[Length(min=2,max=20),DataRequired()])
    email = StringField(label='Email',validators= [Email(),DataRequired()])
    password1= PasswordField(label='Password',validators= [Length(min=6),DataRequired()])
    password2= PasswordField(label='Confirm Password',validators= [EqualTo('password1'),DataRequired()])
    submit=SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username= StringField(label='User Name', validators=[DataRequired()])
    password= PasswordField(label='Password', validators=[DataRequired()])
    submit=SubmitField(label='Sign In')





