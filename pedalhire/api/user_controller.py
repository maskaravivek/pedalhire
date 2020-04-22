from ..constants.global_constants import COMMON_PREFIX
from ..models.base import db
from ..utils.api import handle_response
from ..services.email_service import send_email_with_template
from .authenticate import authenticate
from argon2 import PasswordHasher
from flask import Blueprint, request, abort, session, render_template
import hashlib
import uuid
from pedalhire.cache import cache
from ..services import user_service

user_api = Blueprint('user', __name__)


@user_api.route("/signin", methods=['GET', 'POST'])
def signin_user_api():
    session["logged_in"] = False
    return render_template("login.html")


@user_api.route("/signup", methods=['GET', 'POST'])
def signup_user_api():
    session["logged_in"] = False
    return render_template("signup.html")
