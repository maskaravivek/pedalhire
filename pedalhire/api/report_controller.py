from ..constants.global_constants import COMMON_PREFIX
from ..models.base import db
from ..utils.api import handle_response
from .authenticate import authenticate
from flask import Blueprint, request, abort
import hashlib
import uuid
from pedalhire.cache import cache
from ..utils.api import docache

report_api = Blueprint('report', __name__)

@report_api.route(COMMON_PREFIX + "/generateReport", methods=['POST'])
def generate_report():
    print("report_api")
    return handle_response()
