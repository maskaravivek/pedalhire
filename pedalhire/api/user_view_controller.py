from flask import Blueprint, render_template
from .authenticate import authenticate
from ..utils.api import handle_response
from ..services import user_service

user_view = Blueprint('user_view', __name__)


@user_view.route("/userLogin", methods=['GET'])
def display_login():
    return render_template("userLogin.html")


@user_view.route("/userRegistration", methods=['GET'])
def display_signup():
    return render_template("userRegistration.html")


@user_view.route("/userProfile", methods=['GET'])
@authenticate
def display_user(*args, **kwargs):
    response = user_service.get_user_by_id(login_id=kwargs['login_id'])
    if kwargs['role'] == 'USER':
        print(response['first_name'])
        return render_template("userDetails.html", response=response)
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Not authorized'
        }
        return handle_response(responseObject, 401)
