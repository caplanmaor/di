from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, SelectMultipleField)
from wtforms.validators import InputRequired, Length

class SignUpForm(FlaskForm):
    username = TextAreaField('User Name',
                                validators=[InputRequired(),
                                            Length(max=200)])
    email = TextAreaField('Email',
                                validators=[InputRequired(),
                                            Length(max=200)])
    password1 = TextAreaField('Password',
                                validators=[InputRequired(),
                                            Length(max=200)])
    password2 = TextAreaField('Password Again',
                                validators=[InputRequired(),
                                            Length(max=200)])
    

class LogInForm(FlaskForm):
    username = TextAreaField('User Name',
                                validators=[InputRequired(),
                                            Length(max=200)])
    password = TextAreaField('Password',
                                validators=[InputRequired(),
                                            Length(max=200)])
