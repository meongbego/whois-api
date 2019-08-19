from flask import request
from flask_restful import Resource, reqparse

import whois
from app.helpers.rest import response
from app.helpers import auth
from app.helpers import common


class Whois(Resource):
    @auth.login_required
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('domain', type=str, required=True)
        args = parser.parse_args()

        domain = args['domain']
        if common.validate_domain(domain) is not True:
            return response(403, message="domain not supported")

        try:
            whois_data = whois.query(domain)
        except Exception as e:
            return response(401, message=str(e))
        else:
            data = {
                "name": whois_data.name,
                "registrar": whois_data.registrar,
                "creation_date": str(whois_data.creation_date),
                "expiration_date": str(whois_data.expiration_date),
                "last_updated": str(whois_data.last_updated),
                "name_servers": list(whois_data.name_servers),
            }
            return response(200, data=data)
