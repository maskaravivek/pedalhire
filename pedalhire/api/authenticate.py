from flask import Blueprint, request
from flask import Flask, Response
from functools import wraps
from ..models.user import User
from ..utils.api import handle_response


def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                responseObject = {
                    'status': 'fail',
                    'message': 'Bearer token malformed.'
                }
                return handle_response(responseObject, 401)
        else:
            token = request.headers.get('token')
            if token:
                auth_token = token
            else:
                auth_token = ''
        if auth_token:
            try:
                user_id, role_type = User.decode_auth_token(auth_token)
                kwargs['user_id'] = user_id
                kwargs['role_type'] = role_type
                kwargs['auth_token'] = auth_token
                return f(*args, **kwargs)
            except ValueError as err:
                responseObject = {
                    'status': 'fail',
                    'message': str(err)
                }
                return handle_response(responseObject, 401)
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return handle_response(responseObject, 401)
    return wrapper