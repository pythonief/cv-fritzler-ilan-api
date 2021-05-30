from sqlalchemy.orm import backref
from app import db
from datetime import datetime
from flask import render_template
# Defining the basic model


class UserInfo(db.Model):

    __tablename__ = 'user_info'

    dni = db.Column(db.String(9), primary_key=True)
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


class Job(db.Model):

    __tablename__ = 'jobs'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_info_id = db.Column(
        db.String(9),
        db.ForeignKey('user_info.dni'),
        nullable=False
    )
    job_name = db.Column(db.String(40), nullable=False)
    company = db.Column(db.String(40), nullable=False)
    city = db.Column(db.String(40), nullable=False)
    date_joined = db.Column(db.DateTime(), nullable=False)
    date_left = db.Column(db.DateTime(), nullable=False)
    current = db.Column(db.Boolean(), default=False)


class Course(db.Model):

    __tablename__ = 'courses'

    id = db.Column(db.Integer, nullable=False, primary_key=True)
    user_info_id = db.Column(
        db.String(9),
        db.ForeignKey('user_info.dni'),
        nullable=False
    )
    course_name = db.Column(db.String(200), nullable=False)
    date_joined = db.Column(db.DateTime(), nullable=False)
    date_completed = db.Column(db.DateTime(), default=None)


class Skill(db.Model):

    __tablename__ = 'skills'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_info_id = db.Column(
        db.String(9),
        db.ForeignKey('user_info.dni'),
        nullable=False
    )
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(200), nullable=False)


class Language(db.Model):

    __tablename__ = 'languages'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_info_id = db.Column(
        db.String(9),
        db.ForeignKey('user_info.dni'),
        nullable=False
    )
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)


class Reference(db.Model):
    __tablename__ = 'references'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_info_id = db.Column(
        db.String(9),
        db.ForeignKey('user_info.dni'),
        nullable=False
    )
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    company = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=False)
