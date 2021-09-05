"""
This file initializes the flask app.
"""
import os
from flask import Flask
from flask_migrate import Migrate
from sqlalchemy_utils import create_database, database_exists
from flask_bootstrap import Bootstrap
from app.models import db
from app.views import views
from app.config import config


def create_app(test_config=None):
    """
    This method creates a flask app object with a
    given configuration.

    Args:
        test_config (dict): Defaults to None.

    Returns:
        app (Flask): Flask app object.
    """
    app = Flask(__name__)
    Bootstrap(app)
    # check environment variables to see which config to load
    env = os.environ.get("FLASK_ENV", "dev")

    if test_config:
        app.config.from_mapping(**test_config)
    else:
        # config dict is from config.py
        app.config.from_object(config[env])

    # create database for development and testing
    if env != "prod":
        db_url = app.config["SQLALCHEMY_DATABASE_URI"]
        if not database_exists(db_url):
            create_database(db_url)

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(views.flask_app)

    return app
