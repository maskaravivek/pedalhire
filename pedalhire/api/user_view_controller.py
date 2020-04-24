from flask import Blueprint, request, session, render_template
from .authenticate import authenticate
from ..utils.api import handle_response

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
    if kwargs['role'] == 'USER':
        return render_template("userDetails.html")
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Not authorized'
        }
        return handle_response(responseObject, 401)
