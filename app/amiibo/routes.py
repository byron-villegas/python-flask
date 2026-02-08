from flask import jsonify
from app.amiibo import bp
from app.amiibo import service

@bp.route("/amiibos", methods=["GET"])
def get_amiibos():
    """
    Obtener información de Amiibos
    ---
    tags:
      - Amiibos
    responses:
      200:
        description: Lista de Amiibos obtenida exitosamente
        schema:
          type: object
          properties:
            amiibo:
              type: array
              items:
                $ref: '#/definitions/AmiiboDto'
      500:
        description: Error interno del servidor
    """
    amiibos = service.get_amiibos()

    return jsonify(amiibos)