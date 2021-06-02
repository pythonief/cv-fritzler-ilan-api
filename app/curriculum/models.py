from app import db, ma
from app.base_models import BaseModel
from flask_login.utils import login_required

# Defining the basic model


class Job(BaseModel):

    __tablename__ = 'jobs'

    job_name = db.Column(db.String(40), nullable=False)
    company = db.Column(db.String(40), nullable=False)
    city = db.Column(db.String(40), nullable=False)
    date_joined = db.Column(db.DateTime(), nullable=False)
    date_left = db.Column(db.DateTime(), nullable=False)
    current = db.Column(db.Boolean(), default=False)


class Course(BaseModel):

    __tablename__ = 'courses'

    course_name = db.Column(db.String(200), nullable=False)
    date_joined = db.Column(db.DateTime(), nullable=False)
    date_completed = db.Column(db.DateTime(), default=None)


class Skill(BaseModel):

    __tablename__ = 'skills'

    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    @staticmethod
    def create_skill(name, description):
        errors = []
        if not name:
            errors.append('field name requiered')
        if not description:
            errors.append('field description required')
        if not errors:
            return Skill(name=name, description=description), errors
        return None, errors

class SkillSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Skill
        load_instance = True

class Language(BaseModel):

    __tablename__ = 'languages'

    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    @staticmethod
    def create_lang(name, description):
        errors = []
        if not name:
            errors.append('field name requiered')
        if not description:
            errors.append('field description required')
        if not errors:
            return Language(name=name, description=description), errors
        return None, errors

class LanguageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Language
        load_instance = True


class Reference(BaseModel):
    __tablename__ = 'references'

    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    company = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
