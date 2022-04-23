from flask import Flask
import random
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import flask_login
import flask_mail

# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True
os.system('set FLASK_APP=run.py')

# Database Connection
db_info = {'host': 'localhost',
           'database': 'crypto',
           'psw': 'postgres',
           'user': 'postgres',
           'port': '5432'}
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Email
app.config['MAIL_SERVER']     = 'smtp.gmail.com'
app.config['MAIL_PORT']       = 587
app.config['MAIL_USE_TLS']    = True
app.config['MAIL_USE_SSL']    = False
app.config['MAIL_USERNAME']   = 'caplanmaor@gmail.com'
app.config['MAIL_PASSWORD'] = 'fgeeppdzdauhceri'
mail = flask_mail.Mail(app)

# Login
login_mngr = flask_login.LoginManager(app)

from webapp import models, routes
def create_app():
    db.init_app(app)
    login_mngr.login_view = 'routes.login'
    login_mngr.init_app(app)
    @login_mngr.user_loader
    def load_user(user_id):
        return models.User.query.get(int(user_id))
