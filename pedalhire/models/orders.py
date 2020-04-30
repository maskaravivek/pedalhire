from sqlalchemy.dialects.postgresql import UUID, ARRAY
from .base import db
from .serializer import CustomSerializerMixin
from .order_status import OrderStatus


class Orders(db.Model, CustomSerializerMixin):
    __tablename__ = 'orders'

    serialize_only = ('id', 'product_id', 'user_id', 'start_date', 'end_date', 'order_status')

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    product_id = db.Column(UUID(as_uuid=True), db.ForeignKey('products.id'), nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    days = db.Column(ARRAY(db.String(5)), nullable=True)
    order_status = db.Column(db.Enum(OrderStatus), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
