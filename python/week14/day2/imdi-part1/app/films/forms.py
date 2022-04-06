from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField)
from wtforms.validators import InputRequired, Length


class Add_film_form(FlaskForm):
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=1, max=100)])
    release_date = TextAreaField('Release Date',
                                validators=[InputRequired(),
                                            Length(max=200)])
    created_in_country = TextAreaField('Created In Country',
                                validators=[InputRequired(),
                                            Length(max=200)])
    avilable_in_countries = TextAreaField('Avilable In Countries',
                                validators=[InputRequired(),
                                            Length(max=200)])
    category = TextAreaField('Category',
                                validators=[InputRequired(),
                                            Length(max=200)])
    director = TextAreaField('Director',
                                validators=[InputRequired(),
                                            Length(max=200)])