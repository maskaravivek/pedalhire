from flask import Blueprint, request, abort, session, render_template
from ..services import user_service
from ..constants.global_constants import COMMON_PREFIX

user_view = Blueprint('user_view', __name__)


@user_view.route("/login", methods=['GET'])
def display_login():
    session["logged_in"] = False
    return render_template("login.html")

@user_view.route("/registration", methods=['GET'])
def display_signup():
    session["logged_in"] = False
    return render_template("registration.html")

@user_view.route("/registration", methods=["POST"])
def process_signup():
    session["logged_in"] = True
    dict = request.form
    user_service.register_user(dict)
    return render_template("product_search.html")


@user_view.route("/product-search", methods=['GET'])
def product_search():
    return render_template("product_search.html")
