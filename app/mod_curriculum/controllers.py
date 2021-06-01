from flask import (
    jsonify,
    request
)
from app import db
from . import curriculum_app
from app.mod_curriculum.models import UserInfo, Course, Job, Skill, Reference, Language
# Views

def create_response_json(message, status_code, **kwargs):
    return jsonify({
        'message': message,
        'status_code': status_code,
        **kwargs
    }), status_code

@curriculum_app.route('/cv', methods=['GET'])
@curriculum_app.route('/cv/<id>', methods=['GET'])
def get_user_info(id=1):
    user = UserInfo.query.filter_by(id=id).first()
    if user is None:
        return create_response_json(f'No existe usuario/curriculum', 404)
    return create_response_json('Found', 200, user=user.to_dict(request))


@curriculum_app.route('/cv', methods=['POST'])
def post_user_info(id=None):
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

@curriculum_app.route('/cv', methods=['PUT'])
@curriculum_app.route('/cv/<id>', methods=['PUT'])
def update_user_info(id=1):
    user = UserInfo.query.filter_by(id=id).first()
    user.full_name = request.form.get('full_name', user.full_name)
    user.descript = request.form.get('descript', user.descript)
    user.adress = request.form.get('adress', user.adress)
    user.email = request.form.get('email', user.email)
    user.phone = request.form.get('phone', user.phone)
    user.nationality = request.form.get('nationality', user.nationality)
    user.dob = request.form.get('dob', user.dob)
    user.city = request.form.get('city', user.city)
    user.about = request.form.get('about', user.about)

    user.save()
    return create_response_json('user updated!', 201, user=user.to_dict(request))


@curriculum_app.route('/cv/<id>', methods=['DELETE'])
def delete_user_info(id):
    user = UserInfo.query.filter_by(id=id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
        return create_response_json('user deleted successfully', 200)
    return create_response_json('', 400)
