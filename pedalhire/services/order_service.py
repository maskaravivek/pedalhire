from ..models.base import db
from ..models.orders import Orders
from ..models.order_status import OrderStatus
import uuid

def complete_purchase(productId, startDateTime, endDateTime, userId):
    try:
        order_id = uuid.uuid4()
        orders = Orders(id=order_id,
                        product_id=productId,
                        user_id=userId,
                        start_date=startDateTime,
                        end_date=endDateTime,
                        order_status=OrderStatus.BOOKED)
        db.session.add(orders)
        db.session.commit()

        return get_order_by_id(id=order_id)
    except Exception as e:
        db.session.rollback()
        raise e


def get_order_by_id(**kwargs):
    return get_order_data(**kwargs).to_dict()


def get_order_data(**kwargs):
    return get_order_query(**kwargs).first_or_404()


def get_order_query(**kwargs):
    return Orders.query.filter_by(**kwargs)
