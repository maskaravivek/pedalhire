import os

if os.name == 'nt':
    SECRET_KEY = os.getenv('SECRET_KEY')
elif os.name == 'posix':
    SECRET_KEY = os.environ('SECRET_KEY')
