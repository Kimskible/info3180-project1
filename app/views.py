"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash,session
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import ProfileForm
from app.models import UserProfile
from werkzeug.utils import secure_filename
import hashlib



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about')
def about():
    """Render the website's about page."""
    return render_template('about.html')

@app.route('/profile', methods=['POST', 'GET'])
def profile():
    myForm = ProfileForm()
    print(myForm)
    
    if request.method == 'POST' :
        if myForm.validate_on_submit():
            first_name = myForm.firstname.data
            last_name = myForm.lastname.data
            location = myForm.location.data
            email = myForm.email.data
            biography = myForm.biography.data
            gender = myForm.gender.data
            file = myForm.photo.data
            name, ext = os.path.splitext(secure_filename(file.filename))
            filename = hashlib.sha256(file.read()).hexdigest() + ext
            file.seek(0)

            file.save(os.path.join(app.instance_path, app.config['UPLOAD_FOLDER'], filename))
            user = UserProfile(first_name,last_name,gender,email,location,biography,filename)
            db.session.add(user)
            db.session.commit()
            render_template('home.html')
            
    return render_template('profileForm.html',form=myForm)

@app.route('/profiles')
def profiles():
    """Render the website's profile page."""
    user_profiles = list(db.session.query(UserProfile).all())
    print(user_profiles)
    return render_template('profiles.html',user_profiles=user_profiles)

@app.route('//<id>')
def (id):
    """Render the website's profile page."""
    user = db.session.query(UserProfile).filter_by(id=int(id)).first()
    if user == None:
        return render_template('404.html'), 404
        
    return render_template('fullProfileView.html',user=user)
    


###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")