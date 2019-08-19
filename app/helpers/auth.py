from functools import wraps
from flask import request
from passlib.hash import pbkdf2_sha256
import os


from app.helpers.rest import response


WHOIS_PASSWORD = os.environ.get("PASSWORD", "admin")


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'X-Whois-Key' not in request.headers:
            return response(401, message="Invalid access key")
        else:
            whoiskey = request.headers['X-Whois-Key']
            if not pbkdf2_sha256.verify(WHOIS_PASSWORD, whoiskey):
                return response(401, message="Invalid access key")
        return f(*args, **kwargs)
    return decorated_function
