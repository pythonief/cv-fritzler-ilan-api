from flask import (
    Blueprint,
    request,
    jsonify
)
from app.mod_curriculum.models import UserInfo, Course, Job, Skill, Reference, Language
curriculum_app = Blueprint('curriculum', __name__, url_prefix='/api')

@curriculum_app.route('/jobs', methods=['GET'])
def get_jobs():
    return 'endpoint de trabajos', 200

@curriculum_app.route('/jobs/add', methods=['POST'])
def add_job():
    return 'endpoint para añadir trabajo', 200

@curriculum_app.route('/jobs/<int:id>', methods=['PUT'])
def update_job(id):
    return 'endpoint para actualizar trabajo', 200

@curriculum_app.route('/jobs/<int:id>', methods=['DELETE'])
def delete_job(id):
    return 'endpoint para eliminar trabajo', 200


