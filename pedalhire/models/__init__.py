from .base import db
import os
from ..utils.config import set_app_config


def init_app(app):
    # initiate the models
    app = set_app_config(app)

    db.init_app(app)
    print("Initiated db...")
