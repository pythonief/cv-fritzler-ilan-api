from os import error
from app.utils import create_json_response, date_parser
from app import db, ma
from app.base_models import BaseModel

# Defining the basic model


class Job(BaseModel):

    __tablename__ = 'jobs'

    job_name = db.Column(db.String(40), nullable=False)
    company = db.Column(db.String(40), nullable=False)
    city = db.Column(db.String(40), nullable=False)
    date_joined = db.Column(db.DateTime(), nullable=False)
    date_left = db.Column(db.DateTime(), nullable=True)
    current = db.Column(db.Boolean(), default=False)

    def create_job(job_name, company, city, date_joined, date_left, current):
        errors = []
        if not job_name:
            errors.append('field job_name requiered')
        if not company:
            errors.append('field company required')
        if not city:
            errors.append('field city required')
        if not date_joined:
            errors.append('field date_joined required')
        if not current:
            errors.append('field current required')

        try:
            date_joined = date_parser(date_joined)
            date_left = date_parser(date_left if date_left else '31-12-2070')
            current = True if current == 'True' or current == 'true' else False
        except Exception:
            errors.append(
                "Date Fields doesn't recognize, expected: 31-12-1970 | 31.12.1970 | 31/12/1970")

        if not errors:
            return Job(
                job_name=job_name,
                company=company,
                city=city,
                date_joined=date_joined,
                date_left=date_left,
                current=current,
            ), errors
        return None, errors


class JobSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Job
        load_instance = True


class Course(BaseModel):

    __tablename__ = 'courses'

    course_name = db.Column(db.String(200), nullable=False)
    date_joined = db.Column(db.DateTime(), nullable=False)
    date_completed = db.Column(db.DateTime(), default=None)

    @staticmethod
    def create_course(course_name, date_joined, date_completed):
        errors = []
        if not course_name:
            errors.append('field course_name requiered')
        if not date_joined:
            errors.append('field date_joined required')
        if not date_completed:
            errors.append('field date_completed required')
        try:
            date_joined = date_parser(date_joined)
            date_joined = date_parser(date_completed)
        except Exception:
            errors.append(
                "Date Fields doesn't recognize, expected: 31-12-1970 | 31.12.1970 | 31/12/1970")
        if not errors:
            return Course(
                course_name=course_name, date_joined=date_joined, date_completed=date_completed), errors
        return None, errors


class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course
        load_instance = True


class Skill(BaseModel):

    __tablename__ = 'skills'

    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.Text, nullable=False)

    @ staticmethod
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

    @ staticmethod
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

    @ staticmethod
    def create_ref(name, email, company, description):
        errors = []
        if not name:
            errors.append('field name requiered')
        if not description:
            errors.append('field description required')
        if not email:
            errors.append('field email requiered')
        if not company:
            errors.append('field company requiered')
        if not errors:
            return Reference(name=name, description=description, email=email, company=company), errors
        return None, errors


class ReferenceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reference
        load_instance = True
