from sqlalchemy.dialects.postgresql import UUID, ARRAY
from .base import db
from .serializer import CustomSerializerMixin
from .order_status import OrderStatus


class Orders(db.Model, CustomSerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    product_id = db.Column(UUID(as_uuid=True), db.ForeignKey('products.id'), nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False)
    start_time = db.Column(db.String(20), nullable=False)
    end_time = db.Column(db.String(20), nullable=False)
    start_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    days = db.Column(ARRAY(db.String(5)), nullable=False)
    order_status = db.Column(db.Enum(OrderStatus), nullable=False)
    created_at = db.Column(db.DateTime(), nullable=False)
    modified_at = db.Column(db.DateTime(), nullable=False)
