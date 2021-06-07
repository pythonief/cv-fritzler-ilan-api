import json
import requests
from app.utils import create_json_response
from oauthlib.oauth2 import WebApplicationClient
from app.auth.models import User, UserSchema
from config import load_secret
from flask import Blueprint, request, redirect
from flask_login.utils import login_required, logout_user
from flask_login import login_user, current_user

GOOGLE_DISCOVER_URL = 'https://accounts.google.com/.well-known/openid-configuration'

auth = Blueprint('auth', __name__, url_prefix='/auth')
client = WebApplicationClient(load_secret('GOOGLE_CLIENT_ID'))
user_schema = UserSchema()

def get_openid_config(uri=GOOGLE_DISCOVER_URL):
    return requests.get(uri).json()


@auth.route('/login', methods=['GET'])
def login():
    openid_config = get_openid_config()
    authorization_uri = client.prepare_request_uri(
        openid_config['authorization_endpoint'],
        request.root_url + 'auth/callback',
        scope=['openid', 'email', 'profile'],
    )
    return redirect(authorization_uri)


@auth.route('/callback', methods=['GET'])
def callback():
    global user_schema
    openid_config = get_openid_config()

    # Obtaining the authorization code
    code = request.args.get('code')

    # Preparing the token request
    token_endpoint = openid_config['token_endpoint']

    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code,
    )
    token_response = requests.post(token_url, headers=headers, data=body, auth=(
        load_secret('GOOGLE_CLIENT_ID'), load_secret('GOOGLE_CLIENT_SECRET')))

    client.parse_request_body_response(json.dumps(token_response.json()))

    # Obtaining the user info from userinfo_endpoint
    userinfo_endpoint = openid_config['userinfo_endpoint']
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    if userinfo_response.json().get('email_verified'):
        user_email = userinfo_response.json().get('email')
        name = f"{userinfo_response.json().get('name')}"
    else:
        return create_json_response("Email isn't verified", 502)
    
    # Creating user
    user = User.exist(user_email)
    if not user:
        user, errors = User.create(user_email, name)
        if errors:
            return create_json_response('', 400, errors=errors)
        user.save()

    login_user(user, remember=True)
    user = user_schema.dump(current_user)
    return create_json_response('Logged in', 200, id=user)


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    try:
        logout_user()
    except Exception as e:
        return create_json_response('Error', 400, error=e)
    return create_json_response('Success Logout', 200)
