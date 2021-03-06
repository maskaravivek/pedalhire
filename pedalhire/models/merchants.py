from sqlalchemy.dialects.postgresql import UUID
from .base import db
from .serializer import CustomSerializerMixin
from ..models.products import Products


class Merchants(db.Model, CustomSerializerMixin):
    __tablename__ = 'merchants'

    serialize_only = ('id', 'first_name', 'last_name', 'phone_extension', 'phone_number', 'address', 'city', 'state', 'country', 'zip_code', 'login_id', 'login.email_id')

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    middle_name = db.Column(db.String(120), nullable=True)
    last_name = db.Column(db.String(120), nullable=False)
    phone_extension = db.Column(db.String(10), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    merchant_photo = db.Column(db.String(1000), nullable=True)
    address = db.Column(db.String(1000), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    state = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    zip_code = db.Column(db.String(20), nullable=False)
    latitude = db.Column(db.String(50), nullable=False)
    longitude = db.Column(db.String(50), nullable=False)
    login_id = db.Column(UUID(as_uuid=True), db.ForeignKey('login.id'), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    products = db.relationship('Products', backref='merchants', uselist=False, lazy= True)
