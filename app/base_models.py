from . import db


class BaseModel(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
