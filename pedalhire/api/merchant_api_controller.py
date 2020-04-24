from flask import Blueprint, request, abort, session
from .authenticate import authenticate
from ..constants.global_constants import COMMON_PREFIX
from ..services import user_service, login_service
from ..utils.api import handle_response

merchant_api = Blueprint('merchant_api', __name__)

@merchant_api.route(COMMON_PREFIX + "/merchant", methods=['POST'])
def create_user_api(*args, **kwargs):
    data = request.json
    response = user_service.create_user(data)
    session.permanent = True
    session['auth_token'] = response['auth_token']
    return handle_response(response)

@merchant_api.route(COMMON_PREFIX + "/merchantLogin", methods=['POST'])
def login_user_api(*args, **kwargs):
    data = request.json
    login_data, token = user_service.login_user(data)
    session['auth_token'] = token
    return handle_response(login_data)

@merchant_api.route(COMMON_PREFIX + "/merchantLogout", methods=['POST'])
@authenticate
def logout_user_api(*args, **kwargs):
    session.pop('auth_token')
    return handle_response({})

@merchant_api.route(COMMON_PREFIX + "/merchant", methods=['PUT'])
@authenticate
def update_user_api(*args, **kwargs):
    abort(404)
    data = request.json
    response = user_service.update_user(data)
    return handle_response(response)


@merchant_api.route(COMMON_PREFIX + "/merchants", methods=['GET'])
@authenticate
def get_all_users_api(*args, **kwargs):
    response = user_service.get_all_users()

    return handle_response(response)

@merchant_api.route(COMMON_PREFIX + "/merchant/<string:user_id>", methods=['GET'])
@authenticate
def get_user_api(user_id, *args, **kwargs):
    response = user_service.get_user_by_id(id=user_id)

    return handle_response(response)

