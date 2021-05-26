from .config import Config
from .config import load_secret


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
