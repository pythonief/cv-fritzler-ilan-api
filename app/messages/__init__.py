from flask import Blueprint

messages = Blueprint('messages', __name__, url_prefix='/message')
