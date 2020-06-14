import os
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import secrets
from os.path import join, dirname, realpath


app = Flask(__name__)
# app.config['SECRET_KEY'] = "secretkey"
app.config['SECRET_KEY'] = secrets.token_urlsafe(32)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://username:password@localhost/dbname"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
# File upload config
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'static/uploads')
db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return UserProfile.get(user_id)

app.config.from_object(__name__)
from app import views
