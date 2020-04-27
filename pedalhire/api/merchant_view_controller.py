from flask import Blueprint, render_template
from .authenticate import authenticate
from ..utils.api import handle_response
from ..services import merchant_service

merchant_view = Blueprint('merchant_view', __name__)


@merchant_view.route("/merchantLogin", methods=['GET'])
def display_login():
    return render_template("merchantLogin.html")


@merchant_view.route("/merchantRegistration", methods=['GET'])
def display_signup():
    return render_template("merchantRegistration.html")


@merchant_view.route("/addProduct", methods=['GET'])
@authenticate
def add_product(*args, **kwargs):
    if kwargs['role'] == 'MERCHANT':
        return render_template("addProduct.html")
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Not authorized'
        }
        return handle_response(responseObject, 401)


@merchant_view.route("/merchantProfile", methods=['GET'])
@authenticate
def display_merchant(*args, **kwargs):
    response = merchant_service.get_merchant_by_id(login_id=kwargs['login_id'])
    if kwargs['role'] == 'MERCHANT':
        return render_template("merchantDetails.html", response=response)
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Not authorized'
        }
        return handle_response(responseObject, 401)
