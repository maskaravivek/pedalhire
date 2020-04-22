from flask import Blueprint, render_template
import uuid
import hashlib
from ..constants.global_constants import COMMON_PREFIX
from ..utils.api import handle_response

root_api = Blueprint('root', __name__)


@root_api.route(COMMON_PREFIX + "/", methods=['GET'])
def get_root_api():
    return render_template('base.html')
