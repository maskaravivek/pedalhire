from ..models.base import db
from ..models.products import Products
from ..models.product_status import ProductStatus
import uuid
from .login_service import register, login


def create_product(data, merchant_id):
    try:
        product_id = uuid.uuid4()
        product = Products(id=product_id,
                           name=data['name'],
                           description=data['description'],
                           merchant_id=merchant_id,
                           price=data['price'],
                           product_photo='',
                           status=ProductStatus.AVAILABLE)
        db.session.add(product)
        db.session.commit()

        return get_product_by_id(id=product_id)
    except Exception as e:
        db.session.rollback()
        raise e


def get_products():
    return Products


def login_merchant(data):
    return login(data)


def update_product(update_data):
    product_id = update_data['id']
    product = get_product_query(id=product_id)
    del update_data['id']
    product.update(update_data)
    db.session.commit()

    return get_product_by_id(id=product_id)


def product_search(latitude, longitude, start_date, end_date):
    result = db.engine.execute("SELECT p.*, s.start_date, s.end_date FROM schedule s INNER JOIN(SELECT p.*, m.distance, m.latitude, m.longitude FROM products p INNER JOIN(SELECT id, latitude, longitude, distance FROM (SELECT merchants.*, calculate_distance(merchants.latitude::numeric, merchants.longitude::numeric, {}, {}, 'K') distance FROM merchants) as m WHERE distance > 7000) m ON m.id = p.merchant_id) p ON (s.product_id = p.id) WHERE s.start_date <= '{}'::date AND s.end_date >= '{}'::date AND NOT EXISTS(SELECT * FROM orders WHERE orders.end_date >= '{}'::date AND orders.end_date <='{}'::date AND orders.product_id = p.id)".format(latitude, longitude, start_date, end_date, start_date, end_date))
    products = []
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
        products.append(product)

    return products


def get_all_products():
    results = Products.query.all()
    return [result.to_dict() for result in results]


def get_product_by_id(**kwargs):
    return get_product_data(**kwargs).to_dict()


def get_product_data(**kwargs):
    return get_product_query(**kwargs).first_or_404()


def get_product_query(**kwargs):
    return Products.query.filter_by(**kwargs)
