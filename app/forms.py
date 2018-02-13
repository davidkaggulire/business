from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextField, PasswordField, SubmitField, RadioField, SelectField, BooleanField
from wtforms.validators import EqualTo, Email, Length,  InputRequired

class SignupForm(FlaskForm):
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm password', validators=[InputRequired(), Length(min=6, max=16)])
    email = StringField('Email', validators=[InputRequired(), Email('Invalid')])
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
    phonenumber = StringField('Phone number')
    submit = SubmitField('Sign Up')

class Loginform(FlaskForm):
    Username = StringField('Username', validators=[InputRequired])
    Password = PasswordField('Password', validators=[InputRequired])
    submit = SubmitField('Login')

class Businessform(FlaskForm):
    Businessname = StringField('Businessname', validators=[InputRequired()])
    Businesscategory = SelectField(choices=[('Automobile','Automobile'), ('Software', 'Software'), ('Aircraft', 'Aircraft'), ('Sales', 'Marketing')])
    Location = StringField('Location', validators=[InputRequired()])
    submit = SubmitField('Register')


