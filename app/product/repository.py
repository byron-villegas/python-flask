import json

from flask import current_app

def get_products():
    file_path = current_app.config.get("APP_DIR") + "/data/products.json"

    f = open(file_path, "r")

    products = json.load(f)

    f.close()

    return products

def save_product(product):
    products = get_products()

    products.append(product)

    file_path = current_app.config.get("APP_DIR") + "/data/products.json"

    f = open(file_path, "w")

    f.write(json.dumps(products, ensure_ascii=False, indent=3))

    f.close()