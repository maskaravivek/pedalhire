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


def get_all_products():
    results = Products.query.all()
    return [result.to_dict() for result in results]


def get_product_by_id(**kwargs):
    return get_product_data(**kwargs).to_dict()


def get_product_data(**kwargs):
    return get_product_query(**kwargs).first_or_404()


def get_product_query(**kwargs):
    return Products.query.filter_by(**kwargs)
