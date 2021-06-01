from app import db
from app.utils import create_json_response
from app.curriculum.models import Course, Job, Skill, Reference, Language
from flask import Blueprint
# Views

curriculum = Blueprint('curriculum', __name__, url_prefix='/api')


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
