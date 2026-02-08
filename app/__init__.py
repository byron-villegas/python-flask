from flask import Flask
from config import Config
from flask_jwt_extended import JWTManager
from flasgger import Swagger


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    jwt = JWTManager(app)

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

    # Register blueprints here
    from app.handlers.exception_handler import bp as bp_exception_handler
    from app.auth import bp as bp_auth
    from app.product import bp as bp_products
    from app.amiibo import bp as bp_amiibo

    app.register_blueprint(bp_exception_handler)
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_products)
    app.register_blueprint(bp_amiibo)

    return app
