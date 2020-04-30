from ..models.base import db
from ..models.merchants import Merchants
from ..models.role import Role
import uuid
from .login_service import register, login
from ..models.product_status import ProductStatus
from ..models.products import Products
from ..services import memcache_service
from ..models.schedule import Schedule


def create_merchant(data):
    try:
        login_id, token = register(data, Role.MERCHANT)
        merchant_id = uuid.uuid4()
        merchant = Merchants(id=merchant_id,
                             login_id=login_id,
                             first_name=data['first_name'],
                             middle_name=data['middle_name'],
                             last_name=data['last_name'],
                             phone_extension=data['phone_extension'],
                             phone_number=data['phone_number'],
                             merchant_photo='',
                             address=data['address'],
                             city=data['city'],
                             state=data['state'],
                             country=data['country'],
                             zip_code=data['zip_code'],
                             latitude=data['latitude'],
                             longitude=data['longitude'])
        db.session.add(merchant)
        db.session.commit()

        user_data = get_merchant_by_id(id=merchant_id)
        user_data['auth_token'] = token
        return user_data
    except Exception as e:
        db.session.rollback()
        raise e


def login_merchant(data):
    return login(data)


def update_merchant(update_data):
    prefix = "m_"
    merchant_id = update_data['id']
    merchant = get_merchant_query(id=merchant_id)
    del update_data['id']
    if 'verified' in update_data:
        del update_data['verified']
    merchant.update(update_data)
    db.session.commit()
    key = prefix + str(merchant_id)
    memcache_service.cache_put(key, update_data)
    return get_merchant_by_id(id=merchant_id)


def get_all_merchants():
    results = Merchants.query.all()
    return [result.to_dict() for result in results]


def get_merchant_by_id(**kwargs):
    prefix = "m_"
    if 'id' in kwargs:
     key = prefix + str(kwargs['id']) 
     exist , value = memcache_service.cache_get(key)
     if  exist :
        return value
     else :
        value = get_merchant_data(**kwargs).to_dict() 
        memcache_service.cache_put(key, value)
        return value
    elif 'login_id' in kwargs:
         key = prefix + str(kwargs['login_id']) 
         exist , value = memcache_service.cache_get(key)
         if  exist :
           return value
         else :
           value = get_merchant_data(**kwargs).to_dict() 
           memcache_service.cache_put(key, value)
           return value
    else:
        return get_merchant_data(**kwargs).to_dict()
    

def get_merchant_data(**kwargs):
    return get_merchant_query(**kwargs).first_or_404()
    
def get_merchant_query(**kwargs):
    return Merchants.query.filter_by(**kwargs)


def add_product(data, login_id):
    try:
        merchant_details = get_merchant_by_id(login_id=login_id)
        product_id = uuid.uuid4()
        product = Products(id=product_id,
                           name=data['name'],
                           description=data['description'],
                           merchant_id=merchant_details['id'],
                           price=data['price'],
                           product_photo="No photo!",
                           status=ProductStatus.AVAILABLE)
        db.session.add(product)
        schedule_id = uuid.uuid4()
        schedule = Schedule(id=schedule_id,
                           product_id=product_id,
                           start_date=data['startDateTime'],
                           end_date=data['endDateTime'])
        db.session.add(schedule)
        db.session.commit()
        
        
    except Exception as e:
        db.session.rollback()
        raise e
