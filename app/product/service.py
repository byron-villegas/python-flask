from app.exceptions.error_negocio_exception import ErrorNegocioException
from app.exceptions.error_tecnico_exception import ErrorTecnicoException
from app.product import repository


def get_products():
    products = repository.get_products()

    return products

def get_product_by_sku(sku: int):
    products = repository.get_products()

    products_filtered = [item for item in products if item["sku"] == sku]

    if len(products_filtered) == 0:
        raise ErrorTecnicoException("EXPYE01", "Product not found")
    
    product = products[0]

    return product

def save_product(product):

    products = repository.get_products()

    products_filtered = [item for item in products if item["sku"] == product["sku"]]

    if len(products_filtered) != 0:
        raise ErrorNegocioException("EXPYE00", "Product already exists")

    repository.save_product(product)

    print(product)