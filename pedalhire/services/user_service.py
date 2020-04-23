from ..models.base import db
from ..models.blacklist_token import BlacklistToken
from flask import abort, request
from ..models.users import Users
from ..models.login import Login
import uuid
from argon2 import PasswordHasher
from .email_service import send_email

ph = PasswordHasher()


def register_user(data):
    check_user = get_user_query(email_id=data['email']).first()
    if not check_user:
        login_id = uuid.uuid4()
        user_id = uuid.uuid4()
        password_hash = ph.hash(data['password'])
        login = Login(id=login_id, email_id=data['email'], password=password_hash)
        db.session.add(login)
        user = Users(id=user_id, first_name=data['firstName'], last_name=data['lastName'],
                     phone_extension=data['countryCode'], phone_number=data['phoneNumber'], address=data['address'],
                     latitude=data['latitude'], longitude=data['longitude'], city=data['city'], state=data['state'],
                     country=data['country'], zip_code=data['zipcode'], login_id=login_id)
        db.session.add(user)
        db.session.commit()

        # generate the auth token
        auth_token = user.encode_auth_token(str(user_id), user.login_id.value)
        return user_id, auth_token.decode()
    else:
        raise Exception('User already exists with this email ID')


def login_user(data):
    user = get_user_data(email_id=data.get('email'))
    if user and ph.verify(user.password, data['password']):
        auth_token = user.encode_auth_token(str(user.id), user.login_id.value)
        if auth_token:
            user_data = user.get_json()
            return user_data, auth_token.decode()


def logout(auth_token):
    blacklist_token = BlacklistToken(token=auth_token)
    db.session.add(blacklist_token)
    db.session.commit()


def reset_user_token(data, reset_token):
    email = data.get('email')
    password_hash = ph.hash(data['password'])

    user = get_user_data(email_id=email, reset_token=reset_token)
    user.reset_token = None
    user.password = password_hash
    db.session.commit()
    return user.get_json()


def send_reset_password_email(email):
    user = get_user_data(email_id=email)
    user.reset_token = uuid.uuid4()
    db.session.commit()

    send_email(
        email=user.email_id,
        subject='Password Reset',
        template='d-78f0ea14466b48b29840e192825cf6d7',
        params={
            'name': email,
            'resetUrl': request.host_url + 'pwReset?email=' + user.email_id + '&reset_token=' + user.reset_token
        }
    )

    return user.get_json()


def update_user(update_data):
    user_id = update_data['id']
    user = get_user_query(id=user_id)
    del update_data['id']
    user.update(update_data)
    db.session.commit()

    return get_user_by_id(id=user_id)


def get_all_users(**kwargs):
    results = get_user_query(**kwargs).all()
    return [result.get_json() for result in results]


def get_user_by_id(**kwargs):
    return get_user_data(**kwargs).get_json()


def get_user_data(**kwargs):
    return get_user_query(**kwargs).first_or_404()


def get_user_query(**kwargs):
    return users.query.filter_by(**kwargs)
