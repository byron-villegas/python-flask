# Python Flask

Proyecto base para aplicaciones Flask con ejemplos de configuración, testing y buenas prácticas.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Variables de Entorno](#variables-de-entorno)
- [Ejecutar Aplicación](#ejecutar-aplicación)
- [Testing](#testing)
- [Tests de Aceptación](#tests-de-aceptación)
- [Tests de Rendimiento](#tests-de-rendimiento)
- [Swagger](#swagger)
- [Links de Referencia](#links-de-referencia)

## Instalación
### Instalar Python
Para instalar python debemos bajarlo e instalarlo de la siguiente pagina https://www.python.org/downloads/

### Crear Entorno Virtual
Para crear el entorno virtual debemos ejecutar el siguiente comando

```shell
python3 -m venv .venv
```

### Usar Envinronment
Se debe ejecutar el siguiente comando

```shell
source .venv/bin/activate
```

### Instalar Dependencias
Para instalar las dependencias debemos ejecutar el siguiente comando

```shell
pip install -r requirements.txt
```

#### Dependencias Exclusivas Windows
Cuando nos encontremos con una depencia exclusiva para windows debemos agregarle **;sys_platform == 'win32'** al final de la version de la dependencia en el archivo **requirements.txt**

Ejemplo

```txt
pywin32==306;sys_platform == 'win32'
```
Entonces cuando instalemos las dependencias del proyecto en un sistema operativo como linux, macOS excluira esa libreria

### Actualizar Dependencias
Para actualizar las dependencias en el archivo **requeriments.txt** debemos ejecutar el siguiente comando

```shell
pip freeze > requirements.txt
```

### Crear Archivo Dependencias Formato JSON
Para crear el archivo de dependencias en formato JSON debemos ejecutar el siguiente comando

```shell
pip list --format json > requirements.json
```

### Listar Dependencias Formato JSON
Se debe ejecutar el siguiente comando

```shell
pip list --format json
```

## Variables de Entorno
Este proyecto utiliza dotenv por lo que podemos crear el archivo **.env** con las siguientes variables

```text
SECRET_KEY=sasfdfsdsdf
JWT_SECRET_KEY=sasfdfssas
```

Estas variables son las llaves secretas que se obtienen por variable de entorno, internamente las usa flask por defecto

## Ejecutar Aplicación
Se debe ejecutar el siguiente comando

```shell
flask --app app run
```

### Docker
A continuacion dejo los comandos a utilizar para generar la imagen y posteriormente ejecutarla

#### Imagen
Para generar la imagen debemos utilizar el siguiente comando

```shell
docker build -t python-flask .
```

#### Ejecutar
Para ejecutar la imagen debemos utilizar el siguiente comando

```shell
docker run -p 5000:5000 python-flask
```

## Testing
### Configuración
Se debe crear un archivo **pyproject.toml** con el siguiente contenido

```python
[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.coverage.run]
branch = true
source = ["config", "app"]
```

Esta configuracion permite definir la ruta de los tests, las carpetas que debe considerar el reporte de cobertura de codigo

### Ejecutar
Se debe ejecutar el siguiente comando

```shell
pytest
```

### Ejecutar con Cobertura
Se debe ejecutar el siguiente comando

```shell
coverage run -m pytest
```

### Generar Reporte Cobertura Formato Consola
Se debe ejecutar el siguiente comando

```shell
coverage report
```

### Generar Reporte Cobertura Formato HTML
Se debe ejecutar el siguiente comando

```shell
coverage html
```

## Tests de Aceptación
### Configuración
Se debe crear un archivo **behave.ini** con el siguiente contenido

```text
[behave.formatters]
html = behave_html_formatter:HTMLFormatter
```

Esto nos permite definir el formato de salida de reporte de los tests de aceptación

### Ejecución
Se debe ejecutar el siguiente comando

```shell
behave acceptance-test/features -f html -o behave-report.html
```

Esta configuracion permite definir donde se encuentran los features, el formato html y el nombre del archivo del reporte

Al finalizar generara un reporte **behave-report.html**

## Tests de Rendimiento
### Configuración
Se debe crear un archivo con el nombre que deseemos, en este caso particular utilice el del mismo proyecto **python-flask.py** con el siguiente contenido

```python
from locust import HttpUser, task, between

wait_time = between(1, 2)

class Product(HttpUser):
    @task
    def get_products(self):
        self.client.get("/products")
    
    @task
    def get_product_by_sku(self):
        self.client.get("/products/15207410")
```
Como podemos ver definimos la tarea, la funcion y a que endpoint deseamos validar

### Ejecución
Se debe ejecutar el siguiente comando

```shell
locust -f performance-test/locust/python-flask.py -H http://localhost:5000 -u 5 -r 10 -t 40 --headless --html locust-report.html
```

Al finalizar generara un reporte **locust-report.html**


## Swagger
### Documentar Modelos
Para documentar los modelos debemos hacerlo mediante el archivo **swagger_schemas.py** 

### Documentar Endpoints
Debemos documentarlo en los **routes.py** de respectivo a continuacion un ejemplo

```python
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
```

### Configurar Swagger UI
Para configurar Swagger UI simplemente agregamos el siguiente codigo al archivo **__init__.py**

```python
    # Flasgger configuration
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": "apispec",
                "route": "/apispec.json",
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/swagger-ui"
    }
    
    # Importar esquemas de Pydantic después de crear la app
    from app.swagger_schemas import get_swagger_definitions
    
    swagger_template = {
        "swagger": "2.0",
        "info": {
            "title": "Python Flask API",
            "description": "API REST con Flask, JWT y documentación automática con DTOs de Pydantic",
            "version": "1.0.0",
            "contact": {
                "name": "API Support",
            }
        },
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT Authorization header usando el esquema Bearer. Ejemplo: 'Bearer {token}'"
            }
        },
        "security": [
            {
                "Bearer": []
            }
        ],
        "definitions": get_swagger_definitions()
    }
    
    Swagger(app, config=swagger_config, template=swagger_template)
```

Cuando ejecutemos a la aplicacion debemos entrar a la pagina **/swagger-ui/**

## Links de Referencia
A continuación dejo links utilizados para realizar este proyecto

[Python Naming Conventions](https://www.geeksforgeeks.org/python-naming-conventions/)

[Configuring Your Flask App](https://dev.to/hackersandslackers/configuring-your-flask-app-2246)

[Flask How To Make Validation On Request JSON](https://stackoverflow.com/questions/61644396/flask-how-to-make-validation-on-request-json-and-json-schema)

[Change Host and Port Of Flask On Run](https://stackoverflow.com/questions/41940663/how-can-i-change-the-host-and-port-that-the-flask-command-uses)

[Performance Testing in Python: A Step-by-Step Guide with Locust](https://code.likeagirl.io/performance-testing-in-python-a-step-by-step-guide-with-flask-e5a56f99513d)

[How To Run Locust](https://appian-locust.readthedocs.io/en/stable/how_to_run_locust.html)

[Behave](https://behave.readthedocs.io/en/latest/tutorial/)
