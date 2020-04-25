from flask import Blueprint, render_template
from .authenticate import authenticate
from ..utils.api import handle_response
from ..services import merchant_service

product_view = Blueprint('product_view', __name__)

@product_view.route("/products", methods=['GET'])
@authenticate
def display_merchant(*args, **kwargs):
    response = merchant_service.get_merchant_by_id(login_id=kwargs['login_id'])
    if kwargs['role'] == 'MERCHANT':
        return render_template("merchantDetails.html", response=response)
