from flask import Flask
from flask.json import jsonify
from configuration import environs

app = Flask(__name__)
app.config.from_object(environs.load_config())


@app.route('/')
def home_page():
    response = {
        'message': 'Bienvenido a la pagina de inicio de mi CVapi',
        'code': '200'
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run()
