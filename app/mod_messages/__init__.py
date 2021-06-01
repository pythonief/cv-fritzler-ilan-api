from flask import Blueprint

mod_messages = Blueprint('messages', __name__, url_prefix='/message')
