from flask import Blueprint, request, abort, session
from .authenticate import authenticate
from ..constants.global_constants import COMMON_PREFIX
from ..services import merchant_service
from ..utils.api import handle_response

merchant_api = Blueprint('merchant_api', __name__)


@merchant_api.route(COMMON_PREFIX + "/merchant", methods=['POST'])
def create_merchant_api(*args, **kwargs):
    data = request.json
    response = merchant_service.create_merchant(data)
    return handle_response(response['auth_token'])


@merchant_api.route(COMMON_PREFIX + "/merchant", methods=['PUT'])
@authenticate
def update_merchant_api(*args, **kwargs):
    abort(404)
    data = request.json
    response = merchant_service.update_merchant(data)
    return handle_response(response)


@merchant_api.route(COMMON_PREFIX + "/merchantLogin", methods=['POST'])
def login_merchant_api(*args, **kwargs):
    data = request.json
    login_data, token = merchant_service.login_merchant(data)
    return handle_response(token)


@merchant_api.route(COMMON_PREFIX + "/merchantLogout", methods=['POST'])
@authenticate
def logout_merchant_api(*args, **kwargs):
    return handle_response({})


@merchant_api.route(COMMON_PREFIX + "/addProduct", methods=['POST'])
@authenticate
def add_product(*args, **kwargs):
    print(kwargs)
    if kwargs['role'] == 'MERCHANT':
        data = request.json
        response = merchant_service.add_product(data, kwargs['login_id'])
        return handle_response(response)
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Not authorized'
        }
        return handle_response(responseObject, 401)
