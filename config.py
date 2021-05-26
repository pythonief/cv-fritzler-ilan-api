"""Flask configuration."""
import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))  
load_dotenv(os.path.join(BASE_DIR, '.env'))


def load_secret(key):
    return os.environ.get(key)


class Config:
    """Base config."""

    def __init__(self):
        SECRET_KEY = load_secret('SECRET_KEY')
        # SESSION_COOKIE_NAME = load_secret('SESSION_COOKIE_NAME') #TODO
        STATIC_FOLDER = 'static'
        TEMPLATES_FOLDER = 'templates'
    

class ProdConfig(Config):
    ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = load_secret('DB_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    


def load_config(mode=load_secret('MODE')):
    if mode == 'dev':
        return DevConfig
    if mode == 'prod':
        return ProdConfig
