# Import the db object from the main application module

from app import db

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
        
        return not bool(list_error), list_error

