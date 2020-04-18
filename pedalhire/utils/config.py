## Used to configure app, be careful
import os

def set_app_config(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgresql+psycopg2://postgres:1234@localhost/postgres')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app
