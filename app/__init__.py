from flask import Blueprint

outer_blueprint = Blueprint('outer', __name__)

from . import outer_views