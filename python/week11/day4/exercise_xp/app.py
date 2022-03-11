from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def home():
    return "welcome"

@app.route("/products")
def products():
    file = open("/home/maor/projects/di/python/week11/day4/exercise_xp/product_db.json")
    text = file.read()
    parsed = json.loads(text)
    product_list = []
    for item in parsed:
        product_list.append(item["Name"])
    return str(product_list)

@app.route("/product_details/<id>")
def details(id=None):
    file = open("/home/maor/projects/di/python/week11/day4/exercise_xp/product_db.json")
    text = file.read()
    parsed = json.loads(text)
    product_list = []
    for item in parsed:
        if item["ProductId"] == id:
            product_list.append(item["Description"])
    return str(product_list)