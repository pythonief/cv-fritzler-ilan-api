from os import name
from flask import (
    Blueprint,
    request,
    jsonify
)
from flask import copy_current_request_context
import threading
from app.mod_messages.models import MessageModel

mod_messages = Blueprint('messages', __name__, url_prefix='/message')


@mod_messages.route('/send', methods=['POST'])
def send_message():
    form = request.form

    valid_message, errors = MessageModel.is_valid(
        {
            'name': form.get('name', ''),
            'phone': form.get('phone', ''),
            'email': form.get('email', ''),
            'message': form.get('message', '')
        }
    )

    if not valid_message:
        return jsonify(errors), 400

    # Save the message in the db
    @copy_current_request_context
    def send_message():
        valid_message.send_email()


    sender = threading.Thread(
        name='mail_sender', 
        target=send_message
    )
    sender.start()

    valid_message.save()
    return jsonify(
        {
            'message': '¡Me pone muy contento que hayas llegado hasta acá! ' +
            'Acabo de mandarte por correo -si es que lo incluiste ;)- ' +
            'mi cv adjunto! No puedo esperar más para poder conocernos y que hablemos ' +
            'del apasionante mundo de la programación. Un saludo cibernauta!',
            'status_code': 201
        }
    ), 201
