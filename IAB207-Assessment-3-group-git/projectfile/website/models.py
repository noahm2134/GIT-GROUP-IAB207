from . import db
from datetime import datetime
from flask_login import UserMixin

class Events(db.Model):
    __tablename__='events' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    created = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    location = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    catagory = db.Column(db.String(20), nullable=False)
    tickets = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(400))
    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='events')
    #username foreign key to let creator update
    user_id = db.Column(db.Integer, db.ForeignKey('users.username'))


class User(db.Model, UserMixin):
    __tablename__='users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    username = db.Column(db.String(100), nullable=False)
    emailid = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)

    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')


class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)   
    qty = db.Column(db.String(3), nullable=False)

    # ... Create the Comments db.relationship
	# relation to call destination.comments and comment.destination
    comments = db.relationship('Comment', backref='bookings')

    
	
    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.now())
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))
    booking_id = db.Column(db.Integer, db.ForeignKey('booking.id'))

    def __repr__(self):
        return "<Comment: {}>".format(self.text)

