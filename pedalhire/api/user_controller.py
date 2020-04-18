from ..constants.global_constants import COMMON_PREFIX
from ..models.base import db
from ..utils.api import handle_response
from ..services.email_service import send_email_with_template
from .authenticate import authenticate
from argon2 import PasswordHasher
from flask import Blueprint, request, abort
import hashlib
import uuid
from pedalhire.cache import cache
from ..services import user_service

user_api = Blueprint('user', __name__)

@user_api.route(COMMON_PREFIX + "/login", methods=['POST'])
def login_user_api():
    data = request.json
    # fetch the user data
    user_data, auth_token  = user_service.login_user(data)
    return handle_response({
        "user_data": user_data,
        "auth_token": auth_token
    })

@user_api.route(COMMON_PREFIX + "/reset/<string:reset_token>", methods=['POST'])
def reset_user_token_api(reset_token):
    data = request.json
    response = user_service.reset_user_token(data, reset_token)
    return handle_response(response)

@user_api.route(COMMON_PREFIX + "/reset", methods=['POST'])
def reset_user_api():
    email = request.json.get('email')
    response = user_service.send_reset_password_email(email)
    return handle_response(response)

@user_api.route(COMMON_PREFIX + "/logout", methods=['POST'])
@authenticate
def logout_user_api(*args, **kwargs):
    user_service.logout(kwargs['auth_token'])
    return handle_response({})


@user_api.route(COMMON_PREFIX + "/users", methods=['GET'])
@authenticate
def get_all_user_api(*args, **kwargs):
    users = user_service.get_all_users()
    return handle_response(users)

@user_api.route(COMMON_PREFIX + "/user/<string:user_id>", methods=['GET'])
@authenticate
def get_user_api(user_id, *args, **kwargs):
    response = user_service.get_user_by_id(id=user_id)
    return handle_response(response)

"""
Update user
"""
@user_api.route(COMMON_PREFIX + "/user", methods=['PUT'])
@authenticate
def update_user_api(*args, **kwargs):
    abort(404)
    data = request.json
    response = user_service.update_user(data)
    return handle_response(response)