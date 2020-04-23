from flask import Blueprint, request, abort
from .authenticate import authenticate
from ..constants.global_constants import COMMON_PREFIX
from ..services import user_service
from ..utils.api import handle_response

user_api = Blueprint('user_api', __name__)

@user_api.route(COMMON_PREFIX + "/user", methods=['POST'])
def create_user_api(*args, **kwargs):
    data = request.json
    response = user_service.create_user(data)
    return handle_response(response)

@user_api.route(COMMON_PREFIX + "/user", methods=['PUT'])
@authenticate
def update_user_api(*args, **kwargs):
    abort(404)
    data = request.json
    response = user_service.update_user(data)
    return handle_response(response)


@user_api.route(COMMON_PREFIX + "/users", methods=['GET'])
def get_all_users_api(*args, **kwargs):
    response = user_service.get_all_users()

    return handle_response(response)

@user_api.route(COMMON_PREFIX + "/user/<string:user_id>", methods=['GET'])
@authenticate
def get_user_api(user_id, *args, **kwargs):
    response = user_service.get_user_by_id(id=user_id)

    return handle_response(response)
