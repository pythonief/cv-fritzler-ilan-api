from app import db
from app.utils import create_json_response
from app.curriculum.models import Skill, SkillSchema
from flask import Blueprint, request
from flask_login import login_required
# Views

curriculum = Blueprint('curriculum', __name__, url_prefix='/api')

# MarshMallow Schemas
skill_schema = SkillSchema()
skills_schema = SkillSchema(many=True)


@curriculum.route('/info', methods=['GET'])
def get_info():
    info = {
        'fullname': 'Ilan Emanuel Fritzler',
        'short_description': 'Jr Backend Development in Python',
        'contact': {
            'address': 'Strobel 4051, Mar del Plata, Argentina',
            'email': 'fritzlerilan@gmail.com',
            'phone': '+542236690789',
        },
        'born': {
            'in': 'Mar del Plata, Buenos Aires, Argentina',
            'dob': '15 June 1994',
        },
        'nationality': 'Argentinian',
        'about': 'Passionate student of Programming with a special interest in ' +
        'the back-end stack. I want to get surrounded for new technologies to ' +
        'improve my skills. I’ve achieved knowledge of Python in the last 6 months.'
    }
    return create_json_response('Success', 200, personal_information=info)


"""
    Skills Views
"""


@curriculum.route('/skills', methods=['GET'])
def get_skills():
    global skills_schema

    skills = Skill.query.all()
    output = skills_schema.dump(skills)

    return create_json_response('Success', 200, skills=output)


@curriculum.route('/skills/<int:id>', methods=['GET'])
def get_skill(id):
    global skill_schema
    try:
        skill = Skill.query.filter_by(id=id).first()
        if skill:
            output = skill_schema.dump(skill)
            return create_json_response('Found', 200, skill=output)
        return create_json_response('', 404)
    except Exception as e:
        return create_json_response('Error', 404, error=e)


@curriculum.route('/skills/add', methods=['POST'])
@login_required
def set_skill():
    global skill_schema

    name = request.form.get('name', None)
    description = request.form.get('description', None)
    valid_skill, list_error = Skill.create_skill(name, description)

    if not valid_skill:
        return create_json_response('Bad request', 400, errors=list_error)

    valid_skill.save()
    skill = skill_schema.dump(valid_skill)
    return create_json_response('Success', 201, skill=skill)


@curriculum.route('/skills/<int:id>', methods=['PUT'])
@login_required
def update_skill(id):
    global skill_schema
    try:
        skill = Skill.query.filter_by(id=id).first()
        if skill:
            skill.name = request.form.get('name', skill.name)
            skill.description = request.form.get(
                'description', skill.description)

            skill.save()
            output = skill_schema.dump(skill)
            return create_json_response('Updated', 200, skill=output)
        return create_json_response('Not Found', 404)
    except Exception as e:
        return create_json_response('Error', 404, error=e)
