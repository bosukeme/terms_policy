from flask import Blueprint, Response, render_template
from flask_restful import Api, Resource


class Home(Resource):
    def get(self):
        return "Home"


class Terms(Resource):
    def get(self):
        return Response(response=render_template('terms.html'))


class Policy(Resource):
    def get(self):
        return Response(response=render_template('policy.html'))


class CallBack(Resource):
    def get(self):
        return Response(response=render_template('call_back.html'))




terms_bp = Blueprint("bot", __name__)

api = Api(terms_bp)

api.add_resource(Home, '/')
api.add_resource(Terms, "/terms")
api.add_resource(Policy, "/policy")
api.add_resource(CallBack, "/callback")
