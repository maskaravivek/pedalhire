from flask import make_response, jsonify, Response, json
from functools import wraps

def handle_response(response={}, status=200):
    return make_response(jsonify(response)), status

def docache(minutes=5):
    """ Flask decorator that allow to set Cache headers. """
    def fwrap(f):
        @wraps(f)
        def wrapped_f(*args, **kwargs):
            r = f(*args, **kwargs)
            rsp = Response(json.dumps(r), content_type='application/json; charset=utf-8')
            rsp.headers.add('Cache-Control', 'public,max-age=%d' % int(60 * minutes))
            return rsp
        return wrapped_f
    return fwrap