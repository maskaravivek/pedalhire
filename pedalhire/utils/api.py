from flask import make_response, jsonify

def handle_response(response={}, status=200):
    return make_response(jsonify(response)), status
