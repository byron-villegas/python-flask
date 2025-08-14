from flask import Blueprint, jsonify
from werkzeug.exceptions import HTTPException

from app.exceptions.error_negocio_exception import ErrorNegocioException
from app.exceptions.error_tecnico_exception import ErrorTecnicoException

bp = Blueprint('exception_handler', __name__)

@bp.app_errorhandler(Exception)
def handle_exception(exception):

    print(f"Exception caught: {exception}")

    if isinstance(exception, HTTPException):
        return exception

    status = 500

    error = dict()
    error["codigo"] = "500"
    error["mensaje"] = "Ha ocurrido un error interno"

    if isinstance(exception, ErrorNegocioException):
        error["codigo"] = exception.codigo
        error["mensaje"] = exception.mensaje
        status = 409

    if isinstance(exception, ErrorTecnicoException):
        error["codigo"] = exception.codigo

    return jsonify(error), status