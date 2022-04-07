from flask import Flask, json
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import os

# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True

# Database Connection
db_info = {'host': 'localhost',
           'database': 'robots',
           'psw': 'postgres',
           'user': 'postgres',
           'port': '5432'}
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Users

def populate():
    filename = os.path.join(app.static_folder, 'data', 'users.json')
    with open(filename) as test_file:
        data = json.load(test_file)
        for i,user in enumerate(data):
            user = Users(name=data[i]["name"],street=data[i]["address"]["street"],city=data[i]["address"]["city"],zipcode=data[i]["address"]["zipcode"])
            db.session.add(user)
            db.session.commit()

populate()

import routes