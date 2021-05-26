from logging import error
from flask import Blueprint, request, jsonify

from app import db

from app.mod_messages.models import MessageModel

mod_messages = Blueprint('messages', __name__, url_prefix='/message')


@mod_messages.route('/send', methods=['POST'])
def send_message():
    form = request.form

    new_message = {
        'name': form.get('name', ''),
        'phone': form.get('phone', ''),
        'email': form.get('email', ''),
        'message': form.get('message', '')
    }
    valid, errors = MessageModel.is_valid(new_message)
    print(errors)
    print(valid)
    if not valid:
        return jsonify(errors), 400
    
    # Save the message in the db
    message = MessageModel(
        new_message.get('name'),
        new_message.get('phone'),
        new_message.get('email'),
        new_message.get('message')
    )
    message.save()

    return jsonify(new_message), 201
