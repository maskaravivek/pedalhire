from sqlalchemy.dialects.postgresql import UUID
from .base import db
from .serializer import CustomSerializerMixin


class Users(db.Model, CustomSerializerMixin):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    first_name = db.Column(db.String(120), unique=True, nullable=False)
    middle_name = db.Column(db.String(120), nullable=True)
    last_name = db.Column(db.String(120), nullable=False)
    phone_extension = db.Column(db.String(10), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    user_photo = db.Column(db.String(1000), nullable=True)
    address = db.Column(db.String(1000), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    login_id = db.Column(UUID(as_uuid=True), db.ForeignKey('login.id'), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), nullable=False)
    modified_at = db.Column(db.DateTime(), nullable=False)
    orders = db.relationship('Orders', backref='user', uselist=False)
