from app import db
from app import login_manager
import flask_login
import json
from requests import Session

class Users(flask_login.UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    password = db.Column(db.String(200))
    is_admin = db.Column(db.Boolean, unique=False, default=False)
    currency = db.column(db.Integer, default=0)
    user_profile = db.relationship("Profiles", backref=db.backref("user_profile", uselist=False))
    posts = db.relationship('Posts', backref='user_posts', lazy='dynamic')
    transactions = db.relationship('Transactions', backref='user_transactions', lazy='dynamic')
    user_deck = db.relationship("Deck", backref=db.backref("user_deck", uselist=False))

    def __init__(self,name,email,password,posts = tuple()):
        self.name = name
        self.email = email
        self.password = password
        self.posts = posts
    
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

class Pokemons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    pokemon_profile = db.relationship("Profiles", backref=db.backref("profile_pokemons", uselist=False))

    def __init__(self,name):
        self.name = name

    def populate_db():
        session = Session()
        url='https://pokeapi.co/api/v2/pokemon?limit=100'
        response = session.get(url)
        data = json.loads(response.text)
        pokemons = data['results']
        for pokemon in pokemons:
            temp_pokemon = Pokemons.query.filter_by(name=pokemon['name']).first()
            if not temp_pokemon:
                pokemon_i = Pokemons(pokemon['name'])
                db.session.add(pokemon_i)
        db.session.commit()        

class Profiles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemons.id'))

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    body = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self,title,body):
        self.title = title
        self.body = body

class Decks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    card_id = db.relationship('Cards', backref='deck_cards', lazy='dynamic')

    def __init__(self,card_id = tuple()):
        self.card_id = card_id

class Cards(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pokemon = db.relationship("Pokemons", backref=db.backref("card_pokemon", uselist=False))
    transactions = db.relationship('Transactions', backref='card_transactions', lazy='dynamic')
    deck_id = db.Column(db.Integer, db.ForeignKey('decks.id'))

    def __init__(self,pokemon,transactions = tuple()):
        self.pokemon = pokemon
        self.transactions = transactions

    def populate_cards():
        session = Session()
        pokemons = Pokemons.query.all()
        for pokemon in pokemons:
            card = Cards()
            card.pokemon.append()
            db.session.add(card)
            db.session.commit()
            
class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_a = db.Column(db.Integer, db.ForeignKey('users.id'))
    cards_a = db.Column(db.Integer, db.ForeignKey('cards.id'))
    currency_a = db.Column(db.Integer, default=0)
    user_b = db.Column(db.Integer, db.ForeignKey('users.id'))
    cards_b = db.Column(db.Integer, db.ForeignKey('cards.id'))
    currency_b = db.Column(db.Integer, default=0)