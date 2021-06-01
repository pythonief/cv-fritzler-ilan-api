import re
from flask import Blueprint, request
from flask_login.utils import login_required, logout_user
from app.utils import create_json_response
from app.auth.models import User
from flask_login import login_user, current_user

auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    remember = request.form.get('remember', False)

    user = User.exist(email)
    if user and user.check_password(password):
        login_user(user, remember=remember)
        return create_json_response('Success', 200)

    return create_json_response('Check your credentials and try again', 401)



@auth.route('/signup', methods=['POST'])
def signup():
    email = request.form.get('email', None)
    name = request.form.get('name', None)
    password = request.form.get('password', None)
    
    new_user, errors = User.create(email, name, password)
    if not errors:
        new_user.save()
        return create_json_response('Success', 201, user=name, state='Created')

    return create_json_response('Error', 400, errors=errors)

@auth.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return create_json_response('Success Logout', 200)
