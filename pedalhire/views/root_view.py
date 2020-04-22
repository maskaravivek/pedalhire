from flask import Blueprint, render_template
from wtforms.fields import DateField
from flask_wtf import Form

root_view = Blueprint('Main Page', __name__)

class MyForm(Form):
    date = DateField(id='datepick')


@root_view.route('/', methods=['POST', 'GET'])
def get_root_api():
    form = MyForm()
    return render_template('index.html', form=form)
