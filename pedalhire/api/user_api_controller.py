from flask import Blueprint, request, abort, session
from .authenticate import authenticate
from ..constants.global_constants import COMMON_PREFIX
from ..services import user_service, product_service, order_service
from ..utils.api import handle_response

user_api = Blueprint('user_api', __name__)


@user_api.route(COMMON_PREFIX + "/user", methods=['POST'])
def create_user_api(*args, **kwargs):
    data = request.json
    response = user_service.create_user(data)
    return handle_response(response['auth_token'])


@user_api.route(COMMON_PREFIX + "/user", methods=['PUT'])
@authenticate
def update_user_api(*args, **kwargs):
    abort(404)
    data = request.json
    response = user_service.update_user(data)
    return handle_response(response)


@user_api.route(COMMON_PREFIX + "/products", methods=['POST'])
@authenticate
def search_products(*args, **kwargs):
    data = request.json
    response = product_service.product_search(data['latitude'], data['longitude'], data['startDate'], data['endDate'])
    return handle_response(response)


@user_api.route(COMMON_PREFIX + "/userLogin", methods=['POST'])
def login_user_api(*args, **kwargs):
    data = request.json
    login_data, token = user_service.login_user(data)
    return handle_response(token)


@user_api.route(COMMON_PREFIX + "/userLogout", methods=['POST'])
@authenticate
def logout_user_api(*args, **kwargs):
    return handle_response({})


@user_api.route(COMMON_PREFIX + "/purchaseProduct", methods=['POST'])
@authenticate
def purchase_product(*args, **kwargs):
    data = request.json
    user_data = user_service.get_user_by_id(login_id=kwargs['login_id'])
    order_service.complete_purchase(data['id'], data['startDateTime'], data['endDateTime'], user_data.get('id'))
    return handle_response({})
