import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    city_name     = wtforms.StringField("Name", [wtforms.validators.DataRequired()])
    city_country = wtforms.StringField("Country", [wtforms.validators.DataRequired()])
    city_area  = wtforms.IntegerField("Area")
    number_inhabitants  = wtforms.IntegerField("Inhabitants", [wtforms.validators.DataRequired()])
    submit   = wtforms.SubmitField("Submit")
