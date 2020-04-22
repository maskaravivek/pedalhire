from ..models.base import db
from ..models.login import Login
from flask import abort, request
import uuid

def get_all_logins(**kwargs):
    results = get_login_query(**kwargs).all()
    return [result.get_json() for result in results]

def get_login_by_id(**kwargs):
    return get_login_data(**kwargs).get_json()

def get_login_data(**kwargs):
    return get_login_query(**kwargs).first_or_404()

def get_login_query(**kwargs):
    return Login.query.filter_by(**kwargs)
