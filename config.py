"""Flask configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


def load_secret(key):
    return environ.get(key)


class Config:
    """Base config."""
    SECRET_KEY = load_secret('SECRET_KEY')
    # SESSION_COOKIE_NAME = load_secret('SESSION_COOKIE_NAME') #TODO
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class ProdConfig(Config):
    ENV = 'production'
    DEBUG = False
    TESTING = False
    # DATABASE_URI = load_secret('PROD_DATABASE_URI') #TODO


class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = True
    # DATABASE_URI = load_secret('DEV_DATABASE_URI') #TODO


def load_config(mode=load_secret('MODE')):
    if mode == 'dev':
        return DevConfig
    if mode == 'prod':
        return ProdConfig
