from flask import Blueprint, request, session, render_template

merchant_view = Blueprint('merchant_view', __name__)


@merchant_view.route("/merchantLogin", methods=['GET'])
def display_login():
    return render_template("merchantLogin.html")


@merchant_view.route("/merchantRegistration", methods=['GET'])
def display_signup():
    return render_template("merchantRegistration.html")
