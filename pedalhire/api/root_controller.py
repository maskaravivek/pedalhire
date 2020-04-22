from flask import Flask, render_template
import uuid
import hashlib
from ..constants.global_constants import COMMON_PREFIX
from ..utils.api import handle_response
from wtforms.fields import DateField
from flask_wtf import Form

root_api = Flask(__name__)

if __name__ == '__main__':
    root_api.run(debug=True)
