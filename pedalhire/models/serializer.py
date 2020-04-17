from sqlalchemy_serializer import SerializerMixin
from uuid import UUID

class CustomSerializerMixin(SerializerMixin):
    serialize_types = (
        (UUID, lambda x: str(x)),
    )