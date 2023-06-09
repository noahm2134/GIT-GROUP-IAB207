from sqlite3 import Date

from xmlrpc.client import DateTime
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField,SubmitField, StringField, PasswordField, DateField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG','JPG','png','jpg'} 

#create a new event 
class EventForm(FlaskForm):
    name = StringField("Event name", validators=[InputRequired()])
   
    description = TextAreaField('Description', validators=[InputRequired()])
    date = DateField("Date", validators=[InputRequired()])
    location = StringField("Location", validators=[InputRequired()])
    status = SelectField('Status', choices=[('Open'), ('Sold-out'), ('Cancelled')], validators=[InputRequired()])
    catagory = SelectField("Catagory", choices=[('Play'), ('Learn'), ('Watch'), ('Other')], validators=[InputRequired()])
    tickets = StringField("Number of tickets available", validators=[InputRequired()])
    image = FileField('Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
    submit = SubmitField("Create")

#makes a booking
class BookingForm(FlaskForm):
    name = StringField("Name", validators=[InputRequired()])
    qty = StringField("Quantity", validators=[InputRequired()])
    submit = SubmitField("Make Booking")


class UpdateForm(FlaskForm):
    name = StringField("Event name", validators=[InputRequired()])
    description = TextAreaField('Description', 
            validators=[InputRequired()])
    date = DateField("Date", validators=[InputRequired()])
    location = StringField("Location", validators=[InputRequired()])
    status = SelectField('Status', choices=[('Open'), ('Sold-out'), ('Cancelled')], validators=[InputRequired()])
    tickets = StringField("Number of tickets available", validators=[InputRequired()])
    catagory = SelectField("Catagory", choices=[('Play'), ('Learn'), ('Watch'), ('Other')], validators=[InputRequired()])
    image = FileField('Image', validators=[
    FileRequired(message='Image cannot be empty'),
    FileAllowed(ALLOWED_FILE, message='Only supports png,jpg,JPG,PNG')])
    submit = SubmitField("Update")

#creates the login information
class LoginForm(FlaskForm):
    username=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    username=StringField("User Name", validators=[InputRequired()])
    name=StringField("Name", validators=[InputRequired()])
    emailid = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    phone = StringField("Contact Number", validators=[InputRequired()])
    address = StringField("Address", validators=[InputRequired()])
    confirm = PasswordField("Confirm Password")

    #submit button
    submit = SubmitField("Register")

class CommentForm(FlaskForm):
  text = TextAreaField('Comment', [InputRequired()], render_kw={'style': 'width: 1050px'},)
  submit = SubmitField('Make Comment')


