from app import db, ma
from app.base_models import BaseModel
from flask_login import UserMixin

class User(BaseModel, UserMixin):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100))
    is_staff = db.Column(db.Boolean, default=False)

    @staticmethod
    def exist(email) -> 'User':
        return User.query.filter_by(email=email).first()

    @staticmethod
    def create(
            email, name, is_staff=None):
        errors = []

        if email is None:
            errors.append('email es requerido')
        if name is None:
            errors.append('name es requerido')

        if not errors:
            registered = User.exist(email)
            if not registered:
                user = User(email=email, name=name, is_staff=is_staff)
                return user, errors
            else:
                errors.append(
                    f'El email "{email}" ya existe en la base de datos')
        return None, errors


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
