"""
This file holds configuration options.
The Development config is default and spins up the application inside
a Docker container. Production config allows the app to be run on Heroku.
"""
import os


class Config:
    """
    Base Configuration
    """

    USER = os.environ.get("POSTGRES_USER")
    PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    HOST = os.environ.get("POSTGRES_HOST")
    DATABASE = os.environ.get("POSTGRES_DB")
    PORT = os.environ.get("POSTGRES_PORT")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DATABASE_URL = f"postgres+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Development Configuration - default config

    Requires the environment variable `FLASK_ENV=dev`
    """

    SQLALCHEMY_DATABASE_URI = Config.DATABASE_URL
    DEBUG = True


class ProductionConfig(Config):
    """
    Production Configuration

    Requires the environment variable `FLASK_ENV=prod`
    """

    SQLALCHEMY_DATABASE_URI = Config.DATABASE_URL

    DEBUG = False


# map the value of `FLASK_ENV` to a configuration
config = {"dev": DevelopmentConfig, "prod": ProductionConfig}
