from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self):
        data = {}
        return {'data': data}
    pass


class Locations(Resource):
    pass


api.add_resource(Users, '/users')
api.add_resource(Locations, '/locations')

if __name__ == '__main__':
    app.run()
