import flask_wtf
import wtforms


class Form(flask_wtf.FlaskForm):
    name     = wtforms.StringField("Name", [wtforms.validators.DataRequired()])
    city = wtforms.StringField("City", [wtforms.validators.DataRequired()])
    submit   = wtforms.SubmitField("Submit")
