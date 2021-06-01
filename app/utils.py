from flask import jsonify

def create_json_response(message, status, **kwargs):
    return jsonify({
        'message': message,
        'status_code': status,
        'data': {
            **kwargs
        }
    }), status