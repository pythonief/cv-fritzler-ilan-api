# Import the db object from the main application module

from app import db
from app import mail
from config import load_secret
from flask_mail import Message
# Defining the basic model


class BaseModel(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)


class MessageModel(BaseModel):

    __tablename__ = 'messages'
    name = db.Column(db.String(40))
    phone = db.Column(db.String(40))
    email = db.Column(db.String(60))
    message = db.Column(db.Text)

    def __init__(self, name, phone, email, message):
        setattr(self, 'name', name)
        setattr(self, 'phone', phone)
        setattr(self, 'email', email)
        setattr(self, 'message', message)

    def __repr__(self):
        return f'{self.email}, message: {self.message[0:10]}...'

    def send_email(self):
        message_to_recipient = Message(
            subject = f'Fritzler Ilan Emanuel CV para {self.name}',
            recipients=[
                self.email,
            ],
            html='<strong>Respuesta</strong>'
        )
        message_to_me = Message(
            subject=f'{self.name} Email: {self.email[0:12]}...',
            recipients=[
                load_secret('MAIL_USERNAME'),
            ],
            body=self.message
        )
        mail.send(message_to_me)
        mail.send(message_to_recipient)

    @staticmethod
    def is_valid(args):
        list_error = []
        if args['name'] == '':
            list_error.append({
                'error': 'Debe incluir el campo "name"'
            })
        if args['email'] == '':
            list_error.append({
                'error': 'Debe incluir el campo "email"'
            })
        if args['message'] == '':
            list_error.append({
                'error': 'Debe incluir el campo "message"'
            })

        if not list_error:
            return MessageModel(args['name'], args['phone'], args['email'], args['message']), list_error
        else:
            return None, list_error
