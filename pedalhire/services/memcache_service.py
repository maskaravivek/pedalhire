# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 15:54:45 2020

@author: Sudesh
"""

import redis
import os
import json


def cache_put(key,data):
    redis_host = os.environ.get('REDISHOST', 'localhost')
    redis_port = int(os.environ.get('REDISPORT', 6379))
    redis_client = redis.Redis(host=redis_host, port=redis_port)
    key = str(key)
    check = redis_client.set(key , json.dumps(data))
    if check :
        redis_client.expire(key , 600)
    else :
       print("Memcache put operation was unsucessful for key = " + key)
    

def cache_get(key):
    redis_host = os.environ.get('REDISHOST', 'localhost')
    redis_port = int(os.environ.get('REDISPORT', 6379))
    redis_client = redis.Redis(host=redis_host, port=redis_port)
    key = str(key)
    check = redis_client.exists(key)
    if check :
       str_json_data = redis_client.get(key)
       return 1 , json.loads(str_json_data)
    else :
       return 0 , 0
    
    

def cache_delete(key):
    redis_host = os.environ.get('REDISHOST', 'localhost')
    redis_port = int(os.environ.get('REDISPORT', 6379))
    redis_client = redis.Redis(host=redis_host, port=redis_port)
    key = str(key)
    check = redis_client.exists(key)
    if check :
       redis_client.delete(key)
    else :
       print("no such" + key + " key exists")
       


