from flask import Blueprint

bp = Blueprint('amiibo', __name__)

from app.amiibo import routes