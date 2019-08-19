from flask_restful import Resource, reqparse
from passlib.hash import pbkdf2_sha256

import os
from app.helpers import rest

WHOIS_USERNAME = os.environ.get("USERNAME", "admin")
WHOIS_PASSWORD = os.environ.get("PASSWORD", "admin")


class SignIn(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('password', type=str, required=True)
        parser.add_argument('username', type=str, required=True)
        args = parser.parse_args()
        username = args['username']
        password = args['password']
        password_hash = pbkdf2_sha256.hash(WHOIS_PASSWORD)
        
        if WHOIS_USERNAME != username:
            rest.response(401, message="Username Not Valid")
        else:
            if not pbkdf2_sha256.verify(password, password_hash):
                return rest.response(401, message="Password Not Valid")
            else:
                data_response = {
                    "X-Whois-Key": password_hash,
                    "username": username
                }
                return rest.response(200, data=data_response, message="Login Success")
