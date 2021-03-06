from sqlalchemy.dialects.postgresql import UUID
from .base import db
from .serializer import CustomSerializerMixin
from .product_status import ProductStatus
from ..models.orders import Orders
from ..models.schedule import Schedule


class Products(db.Model, CustomSerializerMixin):
    __tablename__ = 'products'

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    merchant_id = db.Column(UUID(as_uuid=True), db.ForeignKey('merchants.id'), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    product_photo = db.Column(db.String(1000), nullable=True)
    status = db.Column(db.Enum(ProductStatus), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    schedules = db.relationship('Schedule', backref='products')
    orders = db.relationship('Orders', backref='products')


