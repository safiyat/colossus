from flask import Blueprint

application = Blueprint('application', __name__)
google_blueprint = Blueprint('gogole', __name__)

from . import views
