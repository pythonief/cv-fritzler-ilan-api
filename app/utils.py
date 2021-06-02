from flask import jsonify
import datetime

def create_json_response(message, status, **kwargs):
    return jsonify({
        'message': message,
        'status_code': status,
        'data': {
            **kwargs
        }
    }), status

def date_parser(str_date:str):
    translate_dict = {
        45: 47, # - --> /
        46: 47, # . --> /
    }
    parsed = str_date.translate(translate_dict)
    date = datetime.datetime.strptime(parsed, '%d/%m/%Y')
    return date
