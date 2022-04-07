from flask import render_template, redirect, flash
from models import Users
from app import app
from forms import Form

@app.route('/')
def index():
    # all users
    names = Users.query.all()
    all_users = []
    for user in names:
        all_users.append(user.name)
        all_users.append(user.street)
        all_users.append(user.city)
        all_users.append(user.zipcode)

    # Roscoeview users
    rosco_user = Users.query.filter_by(city='Roscoeview').first()

    # first five
    five_users = Users.query.limit(5).all()

    # zip starts with a 5
    zip_start_5 = Users.query.filter(Users.zipcode.startswith('5')).limit(3).all()
    return render_template("index.html", all_users = all_users, Roscoeview = rosco_user, five=five_users, zipcode=zip_start_5)

@app.route('/login', methods=['GET', 'POST'])
def login():
    formi = Form()
    if formi.validate_on_submit():
        input_name = formi.name.data
        input_city = formi.city.data
        # name_exists = Users.query(Users.exists().where(Users.name == input_name)).scalar()
        name_exists = bool(Users.query.filter_by(name=input_name).first())
        if name_exists == True:
            flash("you are logged in")
            return redirect("http://127.0.0.1:5000/")
        else:
            flash("you need to register first")


    return render_template("login.html", form=formi)