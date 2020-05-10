from flask import Blueprint, request, redirect, url_for
from .authenticate import authenticate
from ..constants.global_constants import COMMON_PREFIX
from ..services import merchant_service, product_service
from ..utils.api import handle_response
from ..services.upload_service import upload_blob
import os
import uuid

merchant_api = Blueprint('merchant_api', __name__)


@merchant_api.route(COMMON_PREFIX + "/merchant", methods=['POST'])
def create_merchant_api(*args, **kwargs):
    data = request.json
    response = merchant_service.create_merchant(data)
    return handle_response(response['auth_token'])


@merchant_api.route(COMMON_PREFIX + "/merchantLogin", methods=['POST'])
def login_merchant_api(*args, **kwargs):
    data = request.json
    login_data, token = merchant_service.login_merchant(data)
    return handle_response(token)


@merchant_api.route(COMMON_PREFIX + "/merchantLogout", methods=['POST'])
@authenticate
def logout_merchant_api(*args, **kwargs):
    return handle_response({})


@merchant_api.route(COMMON_PREFIX + '/addProduct', methods=['POST'])
@authenticate
def add_product(*args, **kwargs):
    if kwargs['role'] == 'MERCHANT':
        print(request.form)
        image = request.files['img']
        image.save(os.path.join('/tmp', image.filename))
        file_name = str(uuid.uuid4()) + '.jpg'

        file_link = 'https://storage.cloud.google.com/images-pedalhire/{}'.format(
            file_name)
        upload_blob('/tmp/' + image.filename, file_name, 'images-pedalhire')
        responseObject = {
            'name': request.form['name'],
            'description': request.form['description'],
            'price': request.form['price'],
            'startDateTime': request.form['startDateTime'],
            'endDateTime': request.form['endDateTime'],
            'file_link': file_link
        }
        response = product_service.add_product(responseObject, kwargs['login_id'])
        return redirect(url_for('Main Page.get_root_view'))
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Not authorized'
        }
        return handle_response(responseObject, 401)
