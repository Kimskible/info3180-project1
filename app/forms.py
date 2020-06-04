from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,TextField,TextAreaField,SelectField,SubmitField
from wtforms.validators import DataRequired, Email,Required

images = ["png","jpg"]
class ProfileForm(FlaskForm):
    firstname = StringField('FName', validators=[DataRequired()])
    lastname = StringField('LName', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    gender = SelectField('Gender', choices = [  (status, status) for status in ["Male","Female"]], validators = [Required()])
    biography = TextAreaField('Message', validators=[DataRequired()])
    photo = FileField('photo', validators=[ FileRequired(),FileAllowed(images, 'Images only!')])
    submit = SubmitField(label='Submit')