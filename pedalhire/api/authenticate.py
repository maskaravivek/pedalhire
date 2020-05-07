from flask import session, request, render_template
from functools import wraps
from ..models.login import Login


def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if request.headers.get('token'):
            try:
                auth_token = request.headers.get('token')
                if auth_token != 'null':
                    login_id, role = Login.decode_auth_token(auth_token)
                    kwargs['login_id'] = login_id
                    kwargs['role'] = role
                    kwargs['auth_token'] = auth_token
                return f(*args, **kwargs)
            except ValueError as err:
                responseObject = {
                    'status': 'fail',
                    'message': str(err)
                }
                return render_template('index.html')
        elif request.args.get('authToken'):
            try:
                auth_token = request.args.get('authToken')
                if auth_token != 'null':
                    login_id, role = Login.decode_auth_token(auth_token)
                    kwargs['login_id'] = login_id
                    kwargs['role'] = role
                    kwargs['auth_token'] = auth_token
                return f(*args, **kwargs)
            except ValueError as err:
                responseObject = {
                    'status': 'fail',
                    'message': str(err)
                }
                return render_template('index.html')
        elif request.form.get('loginId'):
            try:
                auth_token = request.form['loginId']
                if auth_token != 'null':
                    login_id, role = Login.decode_auth_token(auth_token)
                    kwargs['login_id'] = login_id
                    kwargs['role'] = role
                    kwargs['auth_token'] = auth_token
                return f(*args, **kwargs)
            except ValueError as err:
                responseObject = {
                    'status': 'fail',
                    'message': str(err)
                }
                return render_template('index.html')
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return render_template('index.html')

    return wrapper
