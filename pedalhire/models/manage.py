# Import Global Objects
from ..utils.config import set_app_config

# import libraries
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import models
from .base import db
# create app
app = Flask(__name__)
app = set_app_config(app)

# instantiate db migrations
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
db.init_app(app)

if __name__:
    manager.run()  # run db migrations
