Feature: Productos

  Scenario: Obtener Productos
    Given a request url /products
    When the request sends GET
    Then the response status is OK

  Scenario Outline: Obtener Producto por SKU
    Given a request url /products/<SKU>
    When the request sends GET
    Then the response status is <STATUS>

  Examples:
  | SKU      | STATUS                |
  | 15207410 | OK                    |
  | 4234234  | INTERNAL_SERVER_ERROR |

  Scenario Outline: Registrar Producto
    Given a request url /products
      And a request json payload
        """
        {
            "caracteristicas": [
                {
                    "titulo": "Modelo",
                    "valor": "Xbox 360"
                },
                {
                    "titulo": "Capacidad de almacenamiento",
                    "valor": "8GB"
                },
                {
                    "titulo": "Color",
                    "valor": "Negro"
                }
            ],
            "descripcion": "Xbox",
            "id": 7,
            "imagen": "./assets/img/products/xbox.png",
            "marca": "Microsoft",
            "nombre": "Xbox",
            "precio": 200000,
            "sku": <SKU>
        }
        """
    When the request sends POST
    Then the response status is <STATUS>

  Examples:
  | SKU      | STATUS   |
  | 344234   | OK       |
  | 15207410 | CONFLICT |