from flask import Flask, Blueprint
from config import config

outer_blueprint = Blueprint('outer', __name__)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # a blueprint is used to register functionalities accross different packages or files

    # from inner package
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # from package file using outer_blueprint declared before
    from . import outer_views
    app.register_blueprint(outer_blueprint)

    return app