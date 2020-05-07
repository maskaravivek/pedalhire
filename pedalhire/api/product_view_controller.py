from flask import Blueprint, render_template, request
from .authenticate import authenticate
from ..utils.api import handle_response
from ..services import merchant_service, product_service
from urllib.parse import unquote_plus

product_view = Blueprint('product_view', __name__)


@product_view.route("/products", methods=['GET'])
@authenticate
def display_merchant(*args, **kwargs):
    response = merchant_service.get_merchant_by_id(login_id=kwargs['login_id'])
    if kwargs['role'] == 'MERCHANT':
        return render_template("merchantDetails.html", response=response)


@product_view.route("/productResults", methods=['GET'])
@authenticate
def product_results(*args, **kwargs):
    response = product_service.product_search(request.args.get('latitude'), request.args.get('longitude'),
                                              request.args.get('startDate'), request.args.get('endDate'))
    return render_template('productResults.html', response=response)
