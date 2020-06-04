from . import db
from werkzeug.security import generate_password_hash
from sqlalchemy import Integer, Enum, DateTime
import datetime


class UserProfile(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) tablQe, but if we specify __tablename__ we can change it
    # to `user_profiles` (plural) or some other name.
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(255))
    gender = db.Column(db.Enum('Male', 'Female', name='gender'))
    created_date = db.Column(DateTime, default=datetime.datetime.utcnow)
    imagestr = db.Column(db.String(80))
    

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
            
    def __init__(self,first_name,last_name,gender,email,location,biography,filename):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
        self.gender = gender
        self.biography = biography
        self.imagestr  = filename

    def __repr__(self):
        return '<User %r>' % (self.first_name)