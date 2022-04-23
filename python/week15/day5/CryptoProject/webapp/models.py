from webapp import db
import flask_login
from webapp import login_mngr

class User(flask_login.UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, unique=False, default=False)
    coins = db.relationship('User_Currency_J', backref='coins_ref', lazy='dynamic')

    def __init__(self,name,email,password,coins = tuple()):
        self.name = name
        self.email = email
        self.password = password
        self.coins = coins
    
    @login_mngr.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    

class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    symbol = db.Column(db.String(64))
    first_historical_data = db.Column(db.String(64))
    last_historical_data = db.Column(db.String(64))
    is_active = db.Column(db.Integer)
    users = db.relationship('User_Currency_J', backref='users_ref', lazy='dynamic')

    def __init__(self,name,symbol,first_historical_data,last_historical_data,is_active,users = tuple()):
        self.name = name
        self.symbol = symbol
        self.first_historical_data = first_historical_data
        self.last_historical_data = last_historical_data
        self.is_active = is_active
        self.users = users

class User_Currency_J(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'))