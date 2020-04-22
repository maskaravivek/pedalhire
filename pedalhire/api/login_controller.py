from ..constants.global_constants import COMMON_PREFIX
from ..models.base import db
from ..utils.api import handle_response
from .authenticate import authenticate
from flask import Blueprint, request, abort
import hashlib
import uuid
from pedalhire.cache import cache
from ..services import login_service

login_api = Blueprint('login', __name__)

@login_api.route(COMMON_PREFIX + "/login", methods=['GET'])
def get_all_logins_api(*args, **kwargs):
    logins = login_service.get_all_logins()
    return handle_response(logins)
