from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, SelectMultipleField)
from wtforms.validators import InputRequired, Length
from app.models import Film
from flask import Flask
from app import db
import flask_login


class AddFilmForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=1, max=100)])
    created_in_country = TextAreaField('Created In Country',
                                validators=[InputRequired(),
                                            Length(max=200)])
    avilable_in_countries = TextAreaField('Avilable In Countries',
                                validators=[InputRequired(),
                                            Length(max=200)])
    directors = TextAreaField('Directors',
                                validators=[InputRequired(),
                                            Length(max=200)])
    categories = TextAreaField('Categories',
                                validators=[InputRequired(),
                                            Length(max=200)])

class AddDirectorForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired(),
                                             Length(min=1, max=100)])
    last_name = StringField('Last Name', validators=[InputRequired(),
                                             Length(min=1, max=100)])
    films_directed = SelectMultipleField('Films Directed', validators=[InputRequired()])

    def __init__(self, *args, **kwargs):
        super(AddDirectorForm, self).__init__(*args, **kwargs)
        films = Film.query.all()
        names = []
        for film in films:
            names.append(film.title)
        self.films_directed.choices = names