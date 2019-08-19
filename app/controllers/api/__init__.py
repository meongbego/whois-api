from flask import Blueprint
from flask_restful import Api
from .whois import Whois
from .login import *

api_blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_blueprint)


api.add_resource(Whois, "/whois")
api.add_resource(SignIn, "/login")
