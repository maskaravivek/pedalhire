from flask import Blueprint, request, abort, session, render_template
from ..services import user_service
from ..constants.global_constants import COMMON_PREFIX

user_api = Blueprint('user', __name__)


@user_api.route(COMMON_PREFIX + "/login", methods=['GET'])
def display_login():
    session["logged_in"] = False
    return render_template("login.html")


@user_api.route(COMMON_PREFIX + "/login", methods=["POST"])
def process_login():
    session["logged_in"] = False
    data = request.json
    print(data)


@user_api.route(COMMON_PREFIX + "/registration", methods=['GET'])
def display_signup():
    session["logged_in"] = False
    return render_template("registration.html")


@user_api.route(COMMON_PREFIX + "/registration", methods=["POST"])
def process_signup():
    session["logged_in"] = True
    dict = request.form
    user_service.register_user(dict)
    return render_template("product_search.html")


@user_api.route("/product-search", methods=['GET'])
def product_search():
    return render_template("product_search.html")
