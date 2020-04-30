from flask import Blueprint, render_template
from ..constants.global_constants import COMMON_PREFIX
from ..utils.api import handle_response
from .authenticate import authenticate

root_view = Blueprint('Main Page', __name__)


@root_view.route('/', methods=['POST', 'GET'])
def get_root_view():
    return render_template('index.html')


@root_view.route('/_ah/warmup')
def warmup():
    return '', 200, {}


@root_view.route(COMMON_PREFIX + '/retrieveRole', methods=['POST'])
@authenticate
def retrieve_role(*args, **kwargs):
    if 'role' not in kwargs:
        return handle_response("None")
    else:
        role = kwargs['role']
        return handle_response(role)


@root_view.route("/productSearch", methods=['GET'])
@authenticate
def product_search(*args, **kwargs):
    return render_template("product_search.html")
