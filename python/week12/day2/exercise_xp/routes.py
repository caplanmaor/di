from flask import redirect, render_template, url_for
from app import app
from forms import Form

cities = []

@app.route("/form",  methods=['GET', 'POST'])
def form():
    formi = Form()
    if formi.validate_on_submit():
        cities.append(formi.city_name.data)
        return redirect("http://127.0.0.1:5000/home")
    return render_template('index.html', form = formi)

@app.route("/home")
def home():
    return render_template('home.html', cities = cities)