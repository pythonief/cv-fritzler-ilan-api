import datetime
from app import db
from app.base_models import BaseModel
from app.auth.models import User
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


class Language(BaseModel):

    __tablename__ = 'languages'

    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)


class Reference(BaseModel):
    __tablename__ = 'references'

    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    company = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
