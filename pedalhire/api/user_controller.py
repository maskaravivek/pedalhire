from flask import Blueprint, request, abort, session, render_template
from ..services import user_service
from ..utils.api import handle_response

user_api = Blueprint('user', __name__)


@user_api.route("/signin", methods=['GET'])
def display_login():
    session["logged_in"] = False
    return render_template("login.html")


@user_api.route("/signin", methods=["POST"])
def process_login():
    session["logged_in"] = False
    data = request.json
    print(data)


@user_api.route("/signup", methods=['GET'])
def display_signup():
    session["logged_in"] = False
    return render_template("signup.html")


@user_api.route("/signup", methods=["POST"])
def process_signup():
    session["logged_in"] = True
    dict = request.form
    user_service.register_user(dict)
    return render_template("product_search.html")


@user_api.route("/product-search", methods=['GET'])
def product_search():
    return render_template("product_search.html")
