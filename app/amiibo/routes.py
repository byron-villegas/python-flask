from flask import jsonify
from app.amiibo import bp
from app.amiibo import service

@bp.route("/amiibos", methods=["GET"])
def get_amiibos():
    amiibos = service.get_amiibos()

    return jsonify(amiibos)