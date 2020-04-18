from sqlalchemy.dialects.postgresql import UUID
from .base import db
from .constants import SECRET_KEY
import jwt
import datetime
from .serializer import CustomSerializerMixin
from .blacklist_token import BlacklistToken


class Login(db.Model, CustomSerializerMixin):
    __tablename__ = 'login'

    serialize_only = ('login_id', 'email')

    login_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.id'), db.ForeignKey('merchants.id'), primary_key=True)
    email_id = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def encode_auth_token(self, id, role_type):
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': id,
                'role': role_type
            }
            return jwt.encode(
                payload,
                SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            print('error', e)
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, SECRET_KEY)
            is_blacklisted_token = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted_token:
                raise ValueError('Token blacklisted. Please log in again.')
            else:
                return payload['sub'], payload['role']
        except jwt.ExpiredSignatureError:
            raise ValueError('Signature expired. Please log in again.')
        except jwt.InvalidTokenError:
            raise ValueError('Invalid token. Please log in again.')

    def get_json(self):
        result = self.to_dict()
        return result
