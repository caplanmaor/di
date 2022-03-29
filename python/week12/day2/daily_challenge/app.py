from flask import Flask, render_template, redirect
import flask_wtf
import wtforms

app = Flask(__name__)
app.config['SECRET_KEY']= "password123"

class Form(flask_wtf.FlaskForm):
    fname     = wtforms.StringField("First Name", [wtforms.validators.DataRequired()])
    lname = wtforms.StringField("Last Name", [wtforms.validators.DataRequired()])
    age  = wtforms.IntegerField("Age")
    experience  = wtforms.IntegerField("Years of Experience", [wtforms.validators.DataRequired()])
    submit   = wtforms.SubmitField("Submit")

user_data = {}

@app.route("/form",  methods=['GET', 'POST'])
def form():
    formi = Form()
    if formi.validate_on_submit():
        user_data["fname"] = formi.fname.data
        user_data["lname"] = formi.lname.data
        user_data["age"] = formi.age.data
        user_data["experience"] = formi.experience.data
        return redirect("http://127.0.0.1:5000/cv")
    return render_template('index.html', form = formi)

@app.route("/cv")
def cv():
    return render_template('cv.html', fname = user_data["fname"], lname = user_data["lname"], age = user_data["age"], experience = user_data["experience"])