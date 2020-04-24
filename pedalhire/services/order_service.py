# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 21:47:00 2020

@author: Sudesh
"""

from ..models.base import db
from ..models.orders import Orders
from ..models.products import Products
from ..models.schedule import Schedule
from ..models.merchants import Merchants
from decimal import Decimal
from datetime import datetime

from ..models.blacklist_token import BlacklistToken
from flask import abort, request
import uuid
from argon2 import PasswordHasher
from .email_service import send_email
from math import radians, cos, sin, asin, sqrt

 
def distance(latitude1, latitude2, longitude1, longitude2): 
       
    longitude1 = radians(longitude1) 
    longitude2 = radians(longitude2) 
    latitude1 = radians(latitude1) 
    latitude2 = radians(latitude2) 
       
    dlongitude = longitude2 - longitude1  
    dlatitude = latitude2 - latitude1 
    a = sin(dlatitude / 2)**2 + cos(latitude1) * cos(latitude2) * sin(dlongitude / 2)**2
  
    c = 2 * asin(sqrt(a))   
    r = 3956 
    return(c * r)  

def convert_date(date_time):
    date = date_time.spilt()
    list1 = date[0].split('/')
    list2 = date[1].split(':')
    list3 = []
    for l in list1:
        list3.append(l)
    for l in list2:
        list3.append(l)
    
    return list3

def get_list_of_products(data):
    
    print(data)
    m = Merchants(id ='1', login_id = 1, first_name = 'manikanta', middle_name = 'manikanta', last_name = 'manikanta',  address= 'area', city='tempe',state = 'arizona',country = 'usa',zip_code = '85281', latitude = '33.4091985',longitude = '-111.9202964')
    db.session.add(m)
    merchants = get_merchants()
    listofproducts = []
    start_date = convert_date(data['startdatetime'])
    if start_date[5] == 'PM':
       start = int(start_date[3])
       if start < 12 :
          start = start + 12 
    end_date = convert_date(data['enddatetime'])
    if end_date[5] == 'PM':
       end = int(end_date[3])
       if end < 12 :
          end = end + 12
          
    for merchant in merchants:
        print(merchant)
        '''
        if(distance(Decimal(merchant['latitude']), Decimal(merchant['longitude'], data['latitude'], data['longitude'])) <=25 ):
             ProductList = Schedule.query\
             .join(Products, Schedule.product_id == Products.id)\
             .add_columns(Products.id)\
             .filter(Products.merchant_id == merchant['id'])\
             .filter_by(Schedule.start_date < datetime(int(start_date[0]), int(start_date[1]), int(start_date[2]), start, int(start_date[4]), 0), Schedule.end_date >= datetime(int(end_date[0]), int(end_date[1]), int(end_date[2]), end, int(end_date[4]), 0))\
            
             #products = Products.query.filter_by(merchant_id = merchant['id'], User.pub_date < datetime(int(start_date[0]), int(start_date[1]), int(start_date[2]), start, int(start_date[4]), 0), User.pub_date >= datetime(int(end_date[0]), int(end_date[1]), int(end_date[2]), end, int(end_date[4]), 0)).all()
             for product in ProductList:
                 listofproducts.append(get_product_data(id = product['id']).to_dict())
                 return listofproducts
        '''         
   


def get_product_data(**kwargs):
    return Products.query.filter_by(**kwargs)

def get_merchants():
    results = Merchants.query.all()
    return [result.to_dict() for result in results]
'''
def get_user_query(**kwargs):
    return User.query.filter_by(**kwargs)

def get_user_by_id(**kwargs):
    return get_user_data(**kwargs).get_json()

return get_user_query(**kwargs).first_or_404()
'''