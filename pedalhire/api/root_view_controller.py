from flask import Blueprint, render_template
import uuid
import hashlib
from ..constants.global_constants import COMMON_PREFIX
from ..utils.api import handle_response
from wtforms.fields import DateField
from flask import session
from flask_wtf import Form
from .authenticate import authenticate

root_view = Blueprint('Main Page', __name__)


class MyForm(Form):
    date = DateField(id='datepick')


@root_view.route('/', methods=['POST', 'GET'])
def get_root_view():
    form = MyForm()
    return render_template('index.html', form=form)


@root_view.route(COMMON_PREFIX + '/retrieveRole', methods=['POST'])
@authenticate
def retrieve_role(*args, **kwargs):
    print(kwargs)
    session['role'] = kwargs['role']
    return handle_response(kwargs['role'])


@root_view.route("/product-search", methods=['GET'])
def product_search():
    return render_template("product_search.html")
