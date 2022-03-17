from products_data import retrieve_requested_product, retrieve_all_products
from flask import Flask, render_template, Markup
import json
app = Flask(__name__)

cart_items= []

@app.route("/")
def home():
    return "welcome to my store"

@app.route("/products")
def products():
    items = retrieve_all_products()
    html_items = ""
    for item in items:
        html_items += Markup(f'<div class="item"><h2>{item["Name"]}</h2><img class="img" src="/static/{item["ProductPicUrl"]}"><br><a href="/products/{item["ProductId"]}">details</a></div>')
    return render_template('products.html', items=html_items)

@app.route("/products/<id>")
def details(id=None):
    product_details = retrieve_requested_product(id)
    html_details = ""
    html_details += Markup(f'<div class="item"><h2>{product_details["Name"]}</h2><h3>price: {product_details["Price"]}$</h3><img class="img" src="/static/{product_details["ProductPicUrl"]}"><br><a href="/add_product_to_cart/{product_details["ProductId"]}">add to cart</a></div>')
    return html_details

@app.route("/add_product_to_cart/<id>")
def add(id=None):
    cart_items.append(id)
    return f"added item {id} to the cart"

@app.route("/cart")
def cart():
    all_items = retrieve_all_products()
    html_cart_items = ""
    total_price = 0
    for item in all_items:
        for cart_item in cart_items:
            if item["ProductId"] == cart_item:
                html_cart_items += Markup(f'<div class="item"><h2>{item["Name"]}</h2><h3>price: {item["Price"]}$</h3><img class="img" src="/static/{item["ProductPicUrl"]}"><br><a href="/remove_from_cart/{item["ProductId"]}">remove from cart</a></div>')
    return html_cart_items

@app.route("/remove_from_cart/<id>")
def remove(id=None):
    for cart_item in cart_items:
        if cart_item == id:
            cart_items.remove(cart_item)
    return f"item {id} was removed from the cart"