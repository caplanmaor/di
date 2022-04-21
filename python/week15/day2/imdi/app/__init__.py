from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import os
import flask_login

# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True
os.system('set FLASK_APP=run.py')

# Database Connection
db_info = {'host': 'localhost',
           'database': 'imdi',
           'psw': 'postgres',
           'user': 'postgres',
           'port': '5432'}
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Login
login_mngr = flask_login.LoginManager(app)

from app import models, routes
def create_app():
    db.init_app(app)
    login_mngr.login_view = 'routes.login'
    login_mngr.init_app(app)
    @login_mngr.user_loader
    def load_user(user_id):
        return models.User.query.get(int(user_id))
