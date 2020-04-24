from .health_check_api_controller import health_check_api
from .user_api_controller import user_api
from .merchant_api_controller import merchant_api
from .user_view_controller import user_view
from .root_view_controller import root_view
from .login_api_controller import login_api
from .report_api_controller import report_api
from .order_controller import order_api
from flask_bootstrap import Bootstrap
import os

def init_app(app):
    # register api blueprints...
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY
    bootstrap = Bootstrap(app)
    app.register_blueprint(health_check_api)
    app.register_blueprint(user_api)
    app.register_blueprint(user_view)
    app.register_blueprint(root_view)
    app.register_blueprint(login_api)
    app.register_blueprint(report_api)
    app.register_blueprint(merchant_api)
    app.register_blueprint(order_api)
    print("Initiated API...")
