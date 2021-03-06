from flask import Flask
import random
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import flask_login



# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True

os.system('export FLASK_ENV=development')



# Login
login_manager = flask_login.LoginManager(app)


# Database Connection
db_info = {'host': '172.18.0.3',
           'database': 'pokemon_cards',
           'psw': 'postgres',
           'user': 'postgres',
           'port': '5433'}
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# blueprints
from app.users.users import users_bp
app.register_blueprint(users_bp, url_prefix='/users')

from app.profiles.profiles import profiles_bp
app.register_blueprint(profiles_bp, url_prefix='/profiles')

from app.forum.forum import forum_bp
app.register_blueprint(forum_bp, url_prefix='/forum')

from app.trading.trading import trading_bp
app.register_blueprint(trading_bp, url_prefix='/trading')

from app import models

def create_app():
    db.init_app(app)
    login_manager.login_view = 'routes.login'
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(user_id):
        return models.Users.query.get(int(user_id))

with app.app_context():
    db.create_all()
    
models.Pokemons.populate_db()