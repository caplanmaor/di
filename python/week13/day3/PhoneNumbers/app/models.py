from app import db
from sqlalchemy import func

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    address = db.Column(db.String(64), unique=True)
    phonenumbers = db.relationship('Phonenumber', backref='phone_numbers', lazy='dynamic')
    
    def __init__(self,name,email,address,phonenumbers = tuple()):
        self.name = name
        self.email = email
        self.address = address
        self.phonenumbers = phonenumbers

    def __repr__(self):
        return f'<Person: {self.name}>'


class Phonenumber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(64), unique=True)
    person = db.Column(db.Integer, db.ForeignKey('person.id'))

    def __init__(self,number):
        self.number = number

    def __repr__(self):
        return f'<Number: {self.number}>'
