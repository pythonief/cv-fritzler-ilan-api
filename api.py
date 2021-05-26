from flask import Flask
from flask.json import jsonify
from config import load_config

app = Flask(__name__)
app.config.from_object(load_config())


@app.route('/')
def home_page():
    response = {
        'message': 'Bienvenido a la pagina de inicio de mi CVapi',
        'code': '200'
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()
