from app import db
from sqlalchemy import func

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pets = db.relationship('Pet', backref='in_cart', lazy='dynamic')
    
    def __init__(self,pets = tuple()):
        # self.id = id
        self.pets = pets

    def add_to_cart(pet_id):
        pet = Pet.query.filter_by(id=pet_id).first()
        # pet = Pet(id=pet_id)
        cart = Cart()
        cart.pets.append(pet)
        print(cart.pets)
        db.session.add(cart)
        db.session.commit()

    def get_cart():
        cart = Cart.query.all()
        all_pets = []
        for pet in cart:
            pet_id = pet.id
            all_pets.append(pet_id)
        return all_pets

    def get_total():
        cart = Cart.query.all()
        all_pets = []
        for pet in cart:
            pet_id = pet.id
            all_pets.append(pet_id)
        total_price = 0
        for id in all_pets:
            pet = Pet.query.filter_by(id=id).first()
            total_price += pet.price
        return total_price


class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    gender = db.Column(db.String(64))
    breed = db.Column(db.String(64))
    date_of_birth = db.Column(db.DateTime(timezone=True), server_default=func.now())
    details = db.Column(db.String(64))
    price = db.Column(db.Integer)
    image = db.Column(db.String(256))
    cart = db.Column(db.Integer, db.ForeignKey('cart.id'))

    def __repr__(self):
        return f'<Pet: {self.name}>'
