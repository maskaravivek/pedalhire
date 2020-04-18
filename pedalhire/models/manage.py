# Import Global Objects
from ..utils.config import set_app_config

# import libraries
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import models
from .base import db
from .login import Login
from .users import Users
from .merchants import Merchants
from .order_status import OrderStatus
from .product_status import ProductStatus
from .products import Products
from .schedule import Schedule
from .orders import Orders

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
