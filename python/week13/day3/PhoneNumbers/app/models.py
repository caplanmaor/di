from app import db
from sqlalchemy import func

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    address = db.Column(db.String(64), unique=True)
    phonenumbers = db.relationship('Phonenumber', backref='phone_numbers', lazy='dynamic')
    nationality_junc = db.relationship('Junction', backref='person_ref', lazy='dynamic')
    
    def __init__(self,name,email,address,phonenumbers = tuple()):
        self.name = name
        self.email = email
        self.address = address
        self.phonenumbers = phonenumbers
        # self.nationality_junc = nationality_junc

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

class Nationality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nationality = db.Column(db.String(64))
    person_junc = db.relationship('Junction', backref='nationality_ref', lazy='dynamic')

    def __init__(self,nationality = tuple()):
        self.nationality = nationality
        # self.person_junc = person_junc
    
    def __repr__(self):
        return f'<Nationality: {self.nationality}>'

class Junction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    nationality_id = db.Column(db.Integer, db.ForeignKey('nationality.id'))
