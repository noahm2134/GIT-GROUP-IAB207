from multiprocessing import Event
from flask import Blueprint, render_template, request, redirect, url_for
from .models import Events, Comment, User, Booking
from .forms import EventForm, CommentForm, UpdateForm, BookingForm
from . import db
import os
from werkzeug.utils import secure_filename
#additional import:
from flask_login import login_required, current_user

bp = Blueprint('event', __name__, url_prefix='/events') 

@bp.route('/<id>')
def show(id):
    event = Events.query.filter_by(id=id).first()
    user = User.query.filter_by(id=id).first()
    # create the comment form
    cform = CommentForm()    
    return render_template('events/show.html', event=event, form=cform, user=user)

@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
  print('Method type: ', request.method)
  form = EventForm()
  
  if form.validate_on_submit():
    #calls the function that checks and returns image
    db_file_path=check_upload_file(form)
    event=Events(name=form.name.data,created=form.created.data,description=form.description.data, 
    date=form.date.data, location = form.location.data, status=form.status.data, catagory=form.catagory.data, tickets=form.tickets.data, image=db_file_path)
    # add the object to the db session
    db.session.add(event)
    # commits to the database
    db.session.commit()
    print('Successfully created new event', 'success')
    #Always end with redirect when form is valid
    return redirect(url_for('event.create'))
  return render_template('events/create.html', form=form)

@bp.route('/<id>/update', methods = ['GET', 'POST'])
def update(id):
  update = UpdateForm()
  #user_name = update.username.data
  event = db.session.query(Events).filter_by(id=id).first()
  if update.validate_on_submit():
    #call the function that checks and returns image
    db_file_path=check_upload_file_update(update)
    event=Events(name=update.name.data,created=update.created.data,description=update.description.data, 
    date=update.date.data, location = update.location.data, status=update.status.data, catagory=update.catagory.data, tickets=update.tickets.data, image=db_file_path)
    # add the object to the db session
    #db.session.add(event)
    # commit to the database
    db.session.commit()
    print('Successfully updated event', id, event.name)
    #Always end with redirect when form is valid
    return redirect(url_for('event.update', id=event))
  
  return render_template('events/update.html', update=update, event=event)


def check_upload_file_update(update):
  #get file data from form  
  fp=update.image.data
  filename=fp.filename
  #get the current path of the module file… store image file relative to this path  
  BASE_PATH=os.path.dirname(__file__)
  #upload file location – directory of this file/static/image
  upload_path=os.path.join(BASE_PATH,'static/img',secure_filename(filename))
  #store relative path in DB as image location in HTML is relative
  db_upload_path='/website/static/img/' + secure_filename(filename)
  #save the file and return the db upload path  
  fp.save(upload_path)
  return db_upload_path

def check_upload_file(form):
  #get file data from form  
  fp=form.image.data
  filename=fp.filename
  #get the current path of the module file… store image file relative to this path  
  BASE_PATH=os.path.dirname(__file__)
  #upload file location – directory of this file/static/image
  upload_path=os.path.join(BASE_PATH,'static/img',secure_filename(filename))
  #store relative path in DB as image location in HTML is relative
  db_upload_path='/static/img/' + secure_filename(filename)
  #save the file and return the db upload path  
  fp.save(upload_path)
  return db_upload_path

@bp.route('/<event>/comment', methods = ['GET', 'POST'])  
def comment(event):  
    form = CommentForm()  
    #get the event object associated to the page and the comment
    event_obj = Events.query.filter_by(id=event).first()  
    if form.validate_on_submit():  
      #read the comment from the form
      comment = Comment(text=form.text.data,
                        events=event_obj,
                        user=current_user)
      #here the back-referencing works - comment.event is set
      # and the link is created
      db.session.add(comment) 
      db.session.commit() 
      #flashing a message which needs to be handled by the html
      #flash('Your comment has been added', 'success')  
      print('Your comment has been added', 'success') 
    # using redirect sends a GET request to event.show
    return redirect(url_for('event.show', id=event))

#Book Event
@bp.route('/<id>/booking', methods = ['GET', 'POST'])
def makebooking(id):
  book = BookingForm()   
  
  if book.validate_on_submit():
    booking=Booking(name = book.name.data, qty = book.qty.data)
    # add the object to the db session
    
    db.session.add(booking)
    # commits to the database

    db.session.commit()
    print('Booking Successful', 'success', id)
    return redirect(url_for('event.makebooking', id=book))
  return render_template('events/book.html', book=book)
