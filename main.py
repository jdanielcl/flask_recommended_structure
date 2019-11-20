import os
from flask import Flask, Blueprint
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # a blueprint is used to register functionalities accross different packages or files

    # from inner main package
    from app.main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # from app package
    from app import outer_blueprint
    app.register_blueprint(outer_blueprint)

    return app


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
