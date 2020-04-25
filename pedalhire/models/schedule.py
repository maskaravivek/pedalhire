from sqlalchemy.dialects.postgresql import UUID, ARRAY
from .base import db
from .serializer import CustomSerializerMixin


class Schedule(db.Model, CustomSerializerMixin):
    __tablename__ = 'schedule'

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    product_id = db.Column(UUID(as_uuid=True), db.ForeignKey('products.id'), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    days = db.Column(ARRAY(db.String(5)), nullable=False)
