from flask import (
    Blueprint,
    request,
    jsonify
)
from .views import GetUserInfo, PostUserInfo
from app.mod_curriculum.models import UserInfo, Course, Job, Skill, Reference, Language

curriculum_app = Blueprint('curriculum', __name__, url_prefix='/api')

curriculum_app.add_url_rule('/cv/<int:id>', view_func=GetUserInfo.as_view('getuserinfo'))
curriculum_app.add_url_rule('/cv', view_func=PostUserInfo.as_view('postuserinfo'))
