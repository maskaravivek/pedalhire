from flask import Blueprint, request, session, render_template

user_view = Blueprint('user_view', __name__)


@user_view.route("/userLogin", methods=['GET'])
def display_login():
    return render_template("userLogin.html")


@user_view.route("/userRegistration", methods=['GET'])
def display_signup():
    return render_template("userRegistration.html")
