from ..models.base import db
from ..models.products import Products
from ..models.product_status import ProductStatus
import uuid
from ..services import memcache_service
from .login_service import login
from ..services import merchant_service
from ..models.schedule import Schedule


def add_product(data, login_id):
    try:
        merchant_details = merchant_service.get_merchant_by_id(login_id=login_id)
        product_id = uuid.uuid4()
        product = Products(id=product_id,
                           name=data['name'],
                           description=data['description'],
                           merchant_id=merchant_details['id'],
                           price=data['price'],
                           product_photo=data['file_link'],
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


def get_products():
    return Products


def product_search(latitude, longitude, start_date, end_date):
    try:
        prefix = "p_"
        key1 = prefix + str(latitude) + "_" + str(longitude) + \
               "_" + str(start_date) + ":00_" + str(end_date) + ":00"
        list_of_products = memcache_service.cache_get_list(key1)
        if len(list_of_products) > 0:
            return list_of_products
        else:
            result = db.engine.execute(
                "SELECT p.*, s.start_date, s.end_date FROM schedule s INNER JOIN(SELECT p.*, m.distance, m.latitude, m.longitude FROM products p INNER JOIN(SELECT id, latitude, longitude, distance FROM (SELECT merchants.*, calculate_distance(merchants.latitude::numeric, merchants.longitude::numeric, {}, {}, 'K') distance FROM merchants) as m WHERE distance < 7000) m ON m.id = p.merchant_id) p ON (s.product_id = p.id) WHERE s.start_date <= '{}'::date AND s.end_date >= '{}'::date AND NOT EXISTS(SELECT * FROM orders WHERE orders.end_date >= '{}'::date AND orders.end_date <='{}'::date AND orders.product_id = p.id)".format(
                    latitude, longitude, start_date, end_date, start_date, end_date))
            products = []
            locations = []
            for row in result:
                product = {
                    "id": row.id,
                    "name": row.name,
                    "description": row.description,
                    "merchant_id": row.merchant_id,
                    "price": row.price,
                    "product_photo": row.product_photo,
                    "distance": row.distance,
                    "latitude": row.latitude,
                    "longitude": row.longitude,
                    "start_date": row.start_date,
                    "end_date": row.end_date
                }
                location = {
                    "lat": float(row.latitude),
                    "lng": float(row.longitude),
                }
                print(product, flush=True)
                key = prefix + str(row.latitude) + "_" + str(row.longitude) + \
                      "_" + str(row.start_date) + "_" + str(row.end_date)
                memcache_service.cache_put_list(key, product)
                products.append(product)
                locations.append(location)

            return products, locations
    except Exception as e:
        return [], []


def get_all_products():
    results = Products.query.all()
    return [result.to_dict() for result in results]


def get_product_by_id(**kwargs):
    prefix = "p_"
    if 'id' in kwargs:
        key = prefix + str(kwargs['id'])
        exist, value = memcache_service.cache_get(key)
        if exist:
            return value
        else:
            value = get_product_data(**kwargs).to_dict()
            memcache_service.cache_put(key, value)
            return value
    else:
        return get_product_data(**kwargs).to_dict()


def get_product_data(**kwargs):
    prefix = "p_"
    value = get_product_query(**kwargs).first_or_404()
    if 'id' in kwargs:
        key = prefix + str(value['id'])
        memcache_service.cache_put(key, value.to_dict())
    return value


def get_product_query(**kwargs):
    return Products.query.filter_by(**kwargs)
