from ..constants.global_constants import COMMON_PREFIX
from ..models.base import db
from ..models.role import Role
from ..models.login import Login
from ..utils.api import handle_response
from .authenticate import authenticate
from flask import Blueprint, request, abort
import hashlib
import uuid
from ..services import login_service

login_api = Blueprint('login_api', __name__)


@login_api.route(COMMON_PREFIX + "/login", methods=['POST'])
def login():
    data = request.json
    # fetch the user data
    user_data, auth_token = login_service.login(data)
    return handle_response({
        "user_data": user_data,
        "auth_token": auth_token
    })


@login_api.route(COMMON_PREFIX + "/logout", methods=['POST'])
@authenticate
def logout_api(*args, **kwargs):
    login_service.logout(kwargs['auth_token'])
    return handle_response({})


@login_api.route(COMMON_PREFIX + "/logins", methods=['GET'])
@authenticate
def get_all_login_api(*args, **kwargs):
    users = login_service.get_all_logins()
    return handle_response(users)


@login_api.route(COMMON_PREFIX + "/login/<string:login_id>", methods=['GET'])
@authenticate
def get_login_api(login_id, *args, **kwargs):
    response = login_service.get_login_by_id(id=login_id)
    return handle_response(response)


@login_api.route(COMMON_PREFIX + "/login", methods=['PUT'])
@authenticate
def update_login_api(*args, **kwargs):
    abort(404)
    data = request.json
    response = login_service.update_login(data)
    return handle_response(response)
