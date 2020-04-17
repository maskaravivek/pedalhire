from flask import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import UUID, ARRAY, JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.attributes import QueryableAttribute
import enum

db = SQLAlchemy()