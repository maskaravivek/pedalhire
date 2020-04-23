from flask import Blueprint, request, abort
from .authenticate import authenticate
from ..constants.global_constants import COMMON_PREFIX
from ..services import merchant_service
from ..utils.api import handle_response

merchant_api = Blueprint('merchant_api', __name__)

@merchant_api.route(COMMON_PREFIX + "/merchant", methods=['POST'])
def create_merchant_api(*args, **kwargs):
    data = request.json
    response = merchant_service.create_merchant(data)
    return handle_response(response)

@merchant_api.route(COMMON_PREFIX + "/merchant", methods=['PUT'])
@authenticate
def update_merchant_api(*args, **kwargs):
    abort(404)
    data = request.json
    response = merchant_service.update_merchant(data)
    return handle_response(response)


@merchant_api.route(COMMON_PREFIX + "/merchants", methods=['GET'])
@authenticate
def get_all_merchant_api(*args, **kwargs):
    response = merchant_service.get_all_merchants()

    return handle_response(response)

@merchant_api.route(COMMON_PREFIX + "/merchant/<string:merchant_id>", methods=['GET'])
@authenticate
def get_merchant_api(merchant_id, *args, **kwargs):
    response = merchant_service.get_merchant_by_id(id=merchant_id)

    return handle_response(response)
