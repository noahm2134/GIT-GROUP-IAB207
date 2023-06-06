from flask import ( 
    Blueprint, flash, render_template, request, url_for, redirect
) 
from werkzeug.security import generate_password_hash,check_password_hash
from .models import User
from .forms import LoginForm,RegisterForm
from flask_login import login_user, login_required,logout_user
from . import db


#create a blueprint
bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    register = RegisterForm()
    #the validation of form submis is fine
    if (register.validate_on_submit() == True):
            #get username, password and email from the form
            user_name = register.username.data
            pwd = register.password.data
            email = register.emailid.data
            num = register.phone.data
            add = register.address.data
            name = register.name.data
            #check if a user exists
            u1 = User.query.filter_by(username=user_name).first()
            if u1:
                flash('User name already exists, please login')
                return redirect(url_for('auth.authenticate'))
            # don't store the password - create password hash
            pwd_hash = generate_password_hash(pwd)
            #create a new user model object
            new_user = User(name=name, username=user_name, password_hash=pwd_hash, emailid=email, phone=num,address=add )
            db.session.add(new_user)
            db.session.commit()
            #commit to the database and redirect to HTML page
            return redirect(url_for('main.index'))
    #the else is called when there is a get message
    else:
        return render_template('user.html', form=register, heading='Register')


# this is the hint for a login function
@bp.route('/login', methods=['GET', 'POST'])
def authenticate(): #view function
     print('In Login View function')
     login_form = LoginForm()
     error=None
     if(login_form.validate_on_submit()==True):
         user_name = login_form.username.data
         password = login_form.password.data
         u1 = User.query.filter_by(username=user_name).first()
         if u1 is None:
             error='Incorrect user name'
         elif not check_password_hash(u1.password_hash, password): # takes the hash and password
             error='Incorrect password'
         if error is None:
            #all good, set the login_user of flask_login to manage the user
            login_user(u1)
            return redirect(url_for('main.index'))
         else:
             flash(error)
     return render_template('user.html', form=login_form, heading='Login')

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You have been logged out'