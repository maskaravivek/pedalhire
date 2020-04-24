# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:39:41 2020

@author: Sudesh
"""

from ..constants.global_constants import COMMON_PREFIX
from ..models.base import db
import sys
from ..utils.api import handle_response
from ..services.email_service import send_email_with_template
from .authenticate import authenticate
from argon2 import PasswordHasher
from flask import Blueprint, request, abort, session, render_template, redirect
import hashlib
import uuid
from pedalhire.cache import cache
from ..services import order_service

order_api = Blueprint('order', __name__)

'''
@order_api.route('/products', methods = ['POST', 'GET'])
def student():   
       return render_template('showproducts1.html')
'''
@order_api.route("/showproducts" , methods = ['POST', 'GET'])
def getlistitems():
    if request.method == 'POST':
     data = request.form.to_dict()
     print(data, flush = True)
     result = order_service.get_list_of_products(data)
     #result = [{ 'id':'mani', 'id':'mani', 'name':'mani', 'merchant_id':'mani', 'price':'mani', 'product_photo':'mani', 'status':'mani', 'created_at':'mani','updated_at':'mani'},
     #          { 'id':'mani', 'id':'mani', 'name':'mani', 'merchant_id':'mani', 'price':'mani', 'product_photo':'mani', 'status':'mani', 'created_at':'mani','updated_at':'mani'}]
     return render_template('showproducts.html', results = result)
    
   
    
    
    
    
    

'''
@order_api.route(COMMON_PREFIX + "/itemslist", methods=['GET', 'POST'])
  def getlistitems():
    #starttime = 
    #endtime = 
    #startdate =
    #enddate =
    if method == 'POST'
      order_service.get_list_of_products()
    
    return render_template("signup.html")
'''