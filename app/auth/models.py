from app import db
from app.base_models import BaseModel
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(BaseModel, UserMixin):
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

    def check_password(self, password):
        if password:
            return bool(check_password_hash(self.password, password))
        return False

    @staticmethod
    def exist(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def create(
            email, name, password):
        errors = []

        if email is None:
            errors.append('email es requerido')
        if name is None:
            errors.append('name es requerido')
        if password is None:
            errors.append('password es requerido')

        if not errors:
            registered = User.exist(email)
            if not registered:
                user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
                return user, errors
            else:
                errors.append(
                    f'El email "{email}" ya existe en la base de datos')
        return None, errors
    