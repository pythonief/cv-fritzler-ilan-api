from .config import Config


class ProdConfig(Config):
    ENV = 'production'
    DEBUG = False
    TESTING = False
    # DATABASE_URI = super.load_secret('PROD_DATABASE_URI') #TODO


class DevConfig(Config):
    ENV = 'development'
    DEBUG = True
    TESTING = True
    # DATABASE_URI = super.load_secret('DEV_DATABASE_URI') #TODO


def load_config(mode=Config.load_secret('MODE')):
    if mode == 'dev':
        return DevConfig
    if mode == 'prod':
        return ProdConfig
