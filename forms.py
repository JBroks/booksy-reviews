from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired("Please enter a valid username")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password")])
    submit = SubmitField('Sign In')
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired("Username required to complete registration process"), Length(min=5, max=25)])
    email = StringField('Email', validators=[DataRequired("Email address required to complete registration process"), Email("This is not a valid email address")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password"), Length(min=7, max=50)])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired("Please repeat the password"), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    