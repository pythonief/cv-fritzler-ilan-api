from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

@app.route('/')
def home_page():
    response = {
        'message': 'Bienvenido a la pagina de inicio de mi CVapi',
        'code': '200'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
