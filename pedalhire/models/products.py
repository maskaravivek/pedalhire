from sqlalchemy.dialects.postgresql import UUID
from .base import db
from .serializer import CustomSerializerMixin
from .product_status import ProductStatus


class Products(db.Model, CustomSerializerMixin):
    __tablename__ = 'products'

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    merchant_id = db.Column(UUID(as_uuid=True), db.ForeignKey('merchants.id'), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    product_photo = db.Column(db.String(1000), nullable=True)
    status = db.Column(db.Enum(ProductStatus), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    modified_at = db.Column(db.DateTime(), nullable=False)
    schedules = db.relationship('Schedule', backref='product')
    orders = db.relationship('Orders', backref='product')
