from app import app, db
from app.models import Pet, Cart
from flask import redirect, render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pets')
def pets():
    pets = Pet.query.all()
    all_pets = []
    for pet in pets:
        pet_object = {}
        pet_object.update({'id': pet.id, 'name': pet.name, 'gender': pet.gender, 'breed': pet.breed, 'date_of_birth': pet.date_of_birth, 'details': pet.details, 'price': pet.price, 'image': pet.image, 'cart': pet.cart})
        all_pets.append(pet_object)
    return render_template('pets.html', pets=all_pets)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/pet/<id>')
def pet(id):
    pet = Pet.query.filter_by(id=id).first()
    return render_template('pet.html', pet = pet)

@app.route('/add_pet/<id>')
def add_pet(id):
    Cart.add_to_cart(id)
    return redirect('http://127.0.0.1:5000/cart')