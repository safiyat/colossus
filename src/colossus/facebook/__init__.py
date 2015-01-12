from flask import Blueprint
face = Blueprint('face', __name__)
facebook_blueprint = Blueprint('facebook', __name__)

from . import views
