from . import models, api, services, tests
from flask import Flask, make_response, jsonify
from flask_cors import CORS
from os.path import join, isfile
from sentry_sdk.integrations.flask import FlaskIntegration
import sentry_sdk
from .cache import cache
import os
from .constants.env_constants import SENTRY_DSN_API, ENVIRONMENT, VERSION

app = Flask(__name__)
app.config.from_pyfile('flask.cfg')

dsn = SENTRY_DSN_API
if dsn != None:
    sentry_sdk.init(
        dsn=dsn,
        integrations=[FlaskIntegration()],
        environment=ENVIRONMENT,
        release=VERSION
    )

@app.errorhandler(404)
def not_found_error(error):
    return make_response(jsonify({"status": "failure", "message": 'Not Found'})), 404

@app.errorhandler(500)
def internal_error(error):
    models.db.session.rollback()
    return make_response(jsonify({"status": "failure", "message": error.message})), 500

CORS(app)
models.init_app(app)
api.init_app(app)
services.init_app(app)
tests.init_app(app)
cache.init_app(app)
