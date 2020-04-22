import os

if os.name == 'nt':
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SUPPORT_EMAIL = os.getenv('SUPPORT_EMAIL')
    SEND_GRID_API_KEY = os.getenv('SEND_GRID_API_KEY')
    SENTRY_DSN_API = os.getenv('SENTRY_DSN_API')
    ENVIRONMENT = os.getenv('ENVIRONMENT')
    VERSION = os.getenv('VERSION')
elif os.name == 'posix':
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_DATABASE_URI']
    SUPPORT_EMAIL = os.environ['SUPPORT_EMAIL']
    SEND_GRID_API_KEY = os.environ['SEND_GRID_API_KEY']
    SENTRY_DSN_API = os.environ['SENTRY_DSN_API']
    ENVIRONMENT = os.environ['ENVIRONMENT']
    VERSION = os.environ['VERSION']
