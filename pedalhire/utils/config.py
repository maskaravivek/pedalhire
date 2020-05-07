## Used to configure app, be careful
import os
from ..constants.env_constants import SQLALCHEMY_DATABASE_URI

def set_app_config(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = '/tmp'

    return app
