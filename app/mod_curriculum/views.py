from flask import json, request
from flask import jsonify
from flask.views import View
from .models import UserInfo


def create_response_json(message, status_code, **kwargs):
    return jsonify({
        'message': message,
        'status_code': status_code,
        **kwargs
    }), status_code


class GetUserInfo(View):
    methods = ['GET']

    def dispatch_request(self, id):
        user = UserInfo.query.filter_by(id=id).first()

        if user is None:
            return create_response_json(f'No existe usuario/curriculum con el id {id}', 404)
        return create_response_json('Found', 200, user=user.to_dict())


class PostUserInfo(View):
    methods = ['POST']

    def dispatch_request(self):
        user_valid, errors = UserInfo.create_user(
            request.form.get('full_name', None),
            request.form.get('descript', None),
            request.form.get('adress', None),
            request.form.get('email', None),
            request.form.get('phone', None),
            request.form.get('nationality', None),
            request.form.get('dob', None),
            request.form.get('city', None),
            request.form.get('about', None),
        )
        if user_valid:
            user_valid.save()
            return create_response_json('user_info created!', 200)
        else:
            return jsonify(errors), 400