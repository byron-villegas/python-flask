from flask import Flask
from config import Config
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint


def create_app(config_class=Config):
    app = Flask(__name__)

    app.config.from_object(config_class)

    jwt = JWTManager(app)

    swaggerui_blueprint = get_swaggerui_blueprint(
        Config.SWAGGER_URL,
        f'{Config.SWAGGER_FILE}'
    )

    # Swagger UI configuration
    app.register_blueprint(swaggerui_blueprint)

    # Register blueprints here
    from app.handlers.exception_handler import bp as bp_exception_handler
    from app.auth import bp as bp_auth
    from app.product import bp as bp_products

    app.register_blueprint(bp_exception_handler)
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_products)

    return app
