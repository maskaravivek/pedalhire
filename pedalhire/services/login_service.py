from ..models.base import db
from ..models.login import Login
from argon2 import PasswordHasher
import uuid
from ..models.blacklist_token import BlacklistToken
from ..services import memcache_service

ph = PasswordHasher()

def register(data, role_type):
    check_user = get_login_query(email_id=data['email']).first()
    if not check_user:
        login_id = uuid.uuid4()
        password_hash = ph.hash(data['password'])
        login = Login(id=login_id, email_id=data['email'], password=password_hash,
                    role_type=role_type)
        db.session.add(login)
        
        # generate the auth token
        auth_token = login.encode_auth_token(str(login_id), login.role_type.value)
        return login_id, auth_token.decode()
    else:
        raise Exception('Login already exists with this email ID')

def login(data):
    login = get_login_data(email_id=data.get('email'))
    if login and ph.verify(login.password, data['password']):
        auth_token = login.encode_auth_token(str(login.id), login.role_type.value)
        if auth_token:
            user_data = login.to_dict()
            return user_data, auth_token.decode()

def logout(auth_token):
    blacklist_token = BlacklistToken(token=auth_token)
    db.session.add(blacklist_token)
    db.session.commit()

def update_login(update_data):
    prefix = "l_"    
    login_id = update_data['id']
    login = get_login_query(id=login_id)
    del update_data['id']
    login.update(update_data)
    db.session.commit()
    key = prefix + str(login_id)
    memcache_service.cache_put(key, update_data)
    return get_login_by_id(id=login_id)

def get_all_logins(**kwargs):
    results = get_login_query(**kwargs).all()
    return [result.to_dict() for result in results]

def get_login_by_id(**kwargs):
    prefix = "l_"
    if 'id' in kwargs:
     key = prefix + str(kwargs['id'])
     exist , value = memcache_service.cache_get(key)
     if  exist :
        return value
     else :
         value = get_login_data(**kwargs).to_dict()
         memcache_service.cache_put(key, value)
         return value
    else : 
     return get_login_data(**kwargs).to_dict()
    

def get_login_data(**kwargs):
   
    return get_login_query(**kwargs).first_or_404()
       

def get_login_query(**kwargs):
    return Login.query.filter_by(**kwargs)
