from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import load_config
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(load_config())

mail = Mail(app)
db = SQLAlchemy(app)

try:
    from app.auth.controllers import auth as auth_app
    from app.messages.controllers import messages as message_app
    from app.curriculum.controllers import curriculum
    from app.main.controllers import main as main_app
except Exception as e:
    print(e)

app.register_blueprint(auth_app)
app.register_blueprint(message_app)
app.register_blueprint(curriculum)
app.register_blueprint(main_app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from app.auth.models import User

@login_manager.user_loader
def load_user(id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(id))

#db.drop_all()
db.create_all()
