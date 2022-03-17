import json
from math import prod

def retrieve_all_products():
    file = open("/home/maor/projects/di/python/week11/day5/products.json")
    text = file.read()
    parsed = json.loads(text)
    all_products = []
    for item in parsed:
        all_products.append(item)
    return all_products

def retrieve_requested_product(product_id):
    file = open("/home/maor/projects/di/python/week11/day5/products.json")
    text = file.read()
    parsed = json.loads(text)
    requested_product = []
    for item in parsed:
        if item["ProductId"] == product_id:
            return item
    # return requested_product
