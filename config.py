from os import environ, path
from dotenv import load_dotenv

# https://hackersandslackers.com/configure-flask-applications/

# https://www.geeksforgeeks.org/__file__-a-special-variable-in-python/
# https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:
    """Set Flask configuration from .env file."""

    # General Config
    SECRET_KEY = environ.get("SECRET_KEY")


class ProdConfig(Config):
    FLASK_ENV = "production"
    TESTING = False
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")


class DevConfig(Config):
    FLASK_ENV = "development"
    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = environ.get("DB_URL")
