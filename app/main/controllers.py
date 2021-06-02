from flask import jsonify
from flask import Blueprint
from flask_login.utils import login_required, current_user
from app.utils import create_json_response
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return create_json_response('Bienvenido a la pagina de inicio de mi CVapi', 200)

@main.route('/profile')
@login_required
def profile():
    return create_json_response('User profile', 200, user=current_user.email)
