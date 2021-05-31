import datetime
from app import db
from app.base_models import BaseModel
from flask import render_template
# Defining the basic model


class UserInfo(BaseModel):

    __tablename__ = 'user_info'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(80), nullable=False)
    descript = db.Column(db.String(80), nullable=False)
    adress = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    nationality = db.Column(db.String(80), nullable=False)
    dob = db.Column(db.DateTime(), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    about = db.Column(db.Text(), nullable=False)
    jobs = db.relationship(
        'Job', backref='user_info')
    courses = db.relationship(
        'Course', backref='user_info')
    skills = db.relationship(
        'Skill', backref='user_info')
    languages = db.relationship(
        'Language', backref='user_info')
    references = db.relationship(
        'Reference', backref='user_info')

    def __init__(self, full_name, descript,
                 adress, email,
                 phone, nationality,
                 dob, city, about):
        self.full_name = full_name
        self.descript = descript
        self.adress = adress
        self.email = email
        self.phone = phone
        self.nationality = nationality
        self.dob = datetime.datetime.strptime(dob, '%d-%m-%Y')
        self.city = city
        self.about = about

    def to_dict(self):
        return dict(full_name=self.full_name, descript=self.descript,
                    adress=self.adress, email=self.email,
                    phone=self.phone, nationality=self.nationality,
                    dob=self.dob, city=self.city, about=self.about)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)

    @staticmethod
    def create_user(
            full_name, descript,
            adress, email,
            phone, nationality,
            dob, city, about):
        errors = {'errors': []}
        if full_name is None:
            errors['errors'].append('full_name es requerido')
        if descript is None:
            errors['errors'].append('descript es requerido')
        if adress is None:
            errors['errors'].append('adress es requerido')
        if email is None:
            errors['errors'].append('email es requerido')
        if phone is None:
            errors['errors'].append('phone es requerido')
        if nationality is None:
            errors['errors'].append('nationality es requerido')
        if dob is None:
            errors['errors'].append('dob es requerido')
        if city is None:
            errors['errors'].append('city es requerido')
        if about is None:
            errors['errors'].append('about es requerido')

        if not errors['errors']:
            registered = UserInfo.query.filter_by(email=email).first(
            ) or UserInfo.query.filter_by(full_name=full_name).first()
            if not registered:
                user = UserInfo(full_name, descript, adress, email,
                                phone, nationality, dob, city, about)
                return user, errors
            else:
                errors['errors'].append(
                    f'El email "{email}" o el nombre "{full_name}" ya existe en la base de datos, no es posible registrar un curriculum con email o nombre completo repetido')
        return None, errors


class Job(BaseModel):

    __tablename__ = 'jobs'

    user_info_id = db.Column(
        db.Integer,
        db.ForeignKey('user_info.id'),
        nullable=False
    )
    job_name = db.Column(db.String(40), nullable=False)
    company = db.Column(db.String(40), nullable=False)
    city = db.Column(db.String(40), nullable=False)
    date_joined = db.Column(db.DateTime(), nullable=False)
    date_left = db.Column(db.DateTime(), nullable=False)
    current = db.Column(db.Boolean(), default=False)


class Course(BaseModel):

    __tablename__ = 'courses'

    user_info_id = db.Column(
        db.Integer,
        db.ForeignKey('user_info.id'),
        nullable=False
    )
    course_name = db.Column(db.String(200), nullable=False)
    date_joined = db.Column(db.DateTime(), nullable=False)
    date_completed = db.Column(db.DateTime(), default=None)


class Skill(BaseModel):

    __tablename__ = 'skills'

    user_info_id = db.Column(
        db.Integer,
        db.ForeignKey('user_info.id'),
        nullable=False
    )
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(200), nullable=False)


class Language(BaseModel):

    __tablename__ = 'languages'

    user_info_id = db.Column(
        db.Integer,
        db.ForeignKey('user_info.id'),
        nullable=False
    )
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)


class Reference(BaseModel):
    __tablename__ = 'references'

    user_info_id = db.Column(
        db.Integer,
        db.ForeignKey('user_info.id'),
        nullable=False
    )
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    company = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
