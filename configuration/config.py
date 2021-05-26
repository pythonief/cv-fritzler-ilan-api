"""Flask configuration."""
from os import environ, path, pardir
from dotenv import load_dotenv

basedir = path.abspath(
    path.join(
        path.abspath(
            path.dirname(__file__)
        ), 
        pardir # == '..'
    )
)
load_dotenv(path.join(basedir, '.env'))

class Config:
    """Base config."""
    def __init__(self):
        SECRET_KEY = self.load_secret('SECRET_KEY')
        # SESSION_COOKIE_NAME = load_secret('SESSION_COOKIE_NAME') #TODO
        STATIC_FOLDER = 'static'
        TEMPLATES_FOLDER = 'templates'

    @staticmethod
    def load_secret(key):
        return environ.get(key)
