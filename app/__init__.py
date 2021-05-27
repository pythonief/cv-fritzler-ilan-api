from flask import Flask
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import load_config

app = Flask(__name__)
app.config.from_object(load_config())

mail = Mail(app)
db = SQLAlchemy(app)


@app.route('/')
def home_page():
    response = {
        'message': 'Bienvenido a la pagina de inicio de mi CVapi',
        'code': '200'
    }
    return jsonify(response), 200

from app.mod_messages.controllers import mod_messages as message_module

app.register_blueprint(message_module)

db.create_all()
