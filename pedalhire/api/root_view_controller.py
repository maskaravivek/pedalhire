from flask import Blueprint, render_template
import uuid
import hashlib
from ..constants.global_constants import COMMON_PREFIX
from ..utils.api import handle_response
from wtforms.fields import DateField
from flask_wtf import Form

root_view = Blueprint('Main Page', __name__)

class MyForm(Form):
    date = DateField(id='datepick')


@root_view.route('/', methods=['POST', 'GET'])
def get_root_view():
    form = MyForm()
    return render_template('index.html', form=form)
