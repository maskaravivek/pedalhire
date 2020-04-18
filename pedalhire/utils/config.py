## Used to configure app, be careful
import os

def set_app_config(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/pedalhire'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app
