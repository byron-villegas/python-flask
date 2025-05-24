import json

from flask import current_app
from app.exceptions.error_negocio_exception import ErrorNegocioException
from app.exceptions.error_tecnico_exception import ErrorTecnicoException


def get_products():
    products = read_products()

    return products

def get_product_by_sku(sku: int):
    products = read_products()

    products_filtered = [item for item in products if item["sku"] == sku]

    if len(products_filtered) == 0:
        raise ErrorTecnicoException("EXPYE01", "Product not found")
    
    product = products[0]

    return product

def save_product(product):

    products = read_products()

    products_filtered = [item for item in products if item["sku"] == product["sku"]]

    if len(products_filtered) != 0:
        raise ErrorNegocioException("EXPYE00", "Product already exists")

    products.append(product)

    write_products(products)

    print(products)

def read_products():
    file_path = current_app.config.get("APP_DIR") + "/data/products.json"

    f = open(file_path, "r")

    products = json.load(f)

    f.close()

    return products

def write_products(products):
    file_path = current_app.config.get("APP_DIR") + "/data/products.json"

    f = open(file_path, "w")

    f.write(json.dumps(products, ensure_ascii=False, indent=3))

    f.close()