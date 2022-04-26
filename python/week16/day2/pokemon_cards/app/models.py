from app import db
from app import login_manager
import flask_login

class Users(flask_login.UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, unique=False, default=False)
    coins = db.relationship('Users_Currency_J', backref='coins_ref', lazy='dynamic')

    def __init__(self,name,email,password,coins = tuple()):
        self.name = name
        self.email = email
        self.password = password
        self.coins = coins
    
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))