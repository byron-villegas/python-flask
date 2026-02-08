from flask import jsonify, request
from app.product import bp
from app.product import service
from flask import Response
from app.product.dto import ProductDto, CreateProductDto
from pydantic import ValidationError


@bp.route("/products", methods=["GET"])
def get_products():
    """
    Obtener todos los productos
    ---
    tags:
      - Productos
    responses:
      200:
        description: Lista de productos obtenida exitosamente
        schema:
          type: array
          items:
            $ref: '#/definitions/ProductDto'
      500:
        description: Error interno del servidor
    """
    products = service.get_products()

    return jsonify(products)

@bp.route("/products/<int:sku>", methods=["GET"])
def get_product_by_sku(sku: int):
    """
    Obtener producto por SKU
    ---
    tags:
      - Productos
    parameters:
      - name: sku
        in: path
        type: integer
        required: true
        description: SKU del producto a buscar
        example: 123
    responses:
      200:
        description: Producto encontrado
        schema:
          $ref: '#/definitions/ProductDto'
      404:
        description: Producto no encontrado
      500:
        description: Error interno del servidor
    """
    product = service.get_product_by_sku(sku)

    return jsonify(product)

@bp.route("/products", methods=["POST"])
def post_product():
    """
    Crear un nuevo producto
    ---
    tags:
      - Productos
    parameters:
      - name: body
        in: body
        required: true
        description: Datos del producto a crear
        schema:
          $ref: '#/definitions/CreateProductDto'
    responses:
      200:
        description: Producto creado exitosamente
      400:
        description: Datos inválidos
        schema:
          $ref: '#/definitions/ErrorResponse'
      409:
        description: Producto ya existe
      500:
        description: Error interno del servidor
    """
    try:
        # Validar datos de entrada con Pydantic
        product_data = CreateProductDto(**request.json)
        
        # Guardar producto
        service.save_product(product_data.to_dict())
        
        return Response("", 200, mimetype="application/json")
    except ValidationError as e:
        return jsonify({"statusCode": 400, "message": "Datos inválidos", "errors": e.errors()}), 400