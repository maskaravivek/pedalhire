import redis
import os
import json
from uuid import UUID
from datetime import datetime
from dateutil.parser import parse


class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            # if the obj is uuid, we simply return the value of uuid
            return obj.hex
        if isinstance(obj, datetime):
            return obj.__str__()
        return json.JSONEncoder.default(self, obj)


redis_host = os.environ.get('REDISHOST', 'localhost')
redis_port = int(os.environ.get('REDISPORT', 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port)


def cache_put(key, data):
    if not is_redis_available():
        return
    key = str(key)
    check = redis_client.set(key, json.dumps(data, cls=UUIDEncoder))
    if check:
        redis_client.expire(key, 120)
    else:
        print("Memcache put operation was unsucessful for key = " + key)


def is_redis_available():
    try:
        redis_client.ping()
        print('Successfully connected to redis')
        return True
    except redis.exceptions.ConnectionError as r_con_error:
        return False


def cache_get(key):
    key = str(key)
    if is_redis_available() and redis_client.exists(key):
        str_json_data = redis_client.get(key)
        return 1, json.loads(str_json_data)
    else:
        return 0, 0


def cache_delete(key):
    key = str(key)
    if is_redis_available() and redis_client.exists(key):
        redis_client.delete(key)
    else:
        print("no such" + key + " key exists")


def cache_put_list(key, data):
    key = str(key)
    if not is_redis_available():
        return
    print(key, flush=True)
    check = redis_client.lpush(key, json.dumps(data, cls=UUIDEncoder))
    if check:
        redis_client.expire(key, 1000)
    else:
        print("Memcache put operation was unsucessful for key = " + key)


def cache_get_list(key):
    if not is_redis_available():
        return []
    key = str(key)
    l = redis_client.llen(key)
    print(key, flush=True)
    print(l, flush=True)
    list1 = []
    i = 0
    while i < l:
        value = json.loads(redis_client.lindex(key, i))
        str1 = value['start_date']
        datetime1 = parse(str1)
        value['start_date'] = datetime1
        str1 = value['end_date']
        datetime1 = parse(str1)
        value['end_date'] = datetime1
        list1.append(value)
        i = i + 1
    return list1
