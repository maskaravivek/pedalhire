from ..models.base import db
from ..models.users import Users
from ..models.role import Role
import uuid
from .login_service import register, login
from ..services import memcache_service

def create_user(data):
    try:
        login_id, token = register(data, Role.USER)
        user_id = uuid.uuid4()
        user = Users(id=user_id,
                     login_id=login_id,
                     first_name=data['first_name'],
                     middle_name=data['middle_name'],
                     last_name=data['last_name'],
                     phone_extension=data['phone_extension'],
                     phone_number=data['phone_number'],
                     user_photo='',
                     address=data['address'],
                     city=data['city'],
                     state=data['state'],
                     country=data['country'],
                     zip_code=data['zip_code'],
                     latitude=data['latitude'],
                     longitude=data['longitude'])
        db.session.add(user)
        db.session.commit()

        user_data = get_user_by_id(id=user_id)
        user_data['auth_token'] = token
        return user_data
    except Exception as e:
        db.session.rollback()
        raise e


def login_user(data):
    return login(data)


def update_user(update_data):
    prefix = "u_"
    user_id = update_data['id']
    user = get_user_query(id=user_id)
    del update_data['id']
    if 'verified' in update_data:
        del update_data['verified']
    user.update(update_data)
    db.session.commit()
    key = prefix + str(user_id)
    memcache_service.cache_put(key, update_data)
    return get_user_by_id(id=user_id)


def get_all_users():
    results = Users.query.all()
    return [result.to_dict() for result in results]


def get_user_by_id(**kwargs):
    prefix = "u_"
    if 'id' in kwargs:
       key = prefix + str(kwargs['id'])
       exist , value = memcache_service.cache_get(key)
       if  exist :
           return value
       else :
         value = get_user_data(**kwargs).to_dict()
         memcache_service.cache_put(key, value)
         return value
    else:
       return get_user_data(**kwargs).to_dict()  

def get_user_data(**kwargs):
    value = get_user_query(**kwargs).first_or_404()
    return value 


def get_user_query(**kwargs):
    return Users.query.filter_by(**kwargs)
