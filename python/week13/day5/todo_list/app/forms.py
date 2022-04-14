import flask_wtf
import wtforms

class AddTodo(flask_wtf.FlaskForm):
    details     = wtforms.StringField("Details", [wtforms.validators.DataRequired()])
    submit   = wtforms.SubmitField("Submit")
