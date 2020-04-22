from .health_check_controller import health_check_api
from .user_controller import user_api
from .root_controller import root_api
from .login_controller import login_api
from flask_bootstrap import Bootstrap
import os

def init_app(app):
    # register api blueprints...
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    bootstrap = Bootstrap(app)
    app.register_blueprint(health_check_api)
    app.register_blueprint(user_api)
    app.register_blueprint(root_api)
    app.register_blueprint(login_api)
    print("Initiated API...")
