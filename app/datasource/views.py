# -*- coding: utf-8 -*-

from flask import redirect, request
from . import ds
from flask_login import current_user, login_user, login_required
from .query import Query
from flask_restful import reqparse, Resource

@ds.route('/query', methods=['GET'])
@login_required
def query():
    query = Data()
    # query.query()


class Data(Resource):
    """
    Restful for query
    """
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided', location='json')
        self.reqparse.add_argument('description', type=str, default="", location = 'json')
        super(Data, self).__init__()

    def get(self):
        pass

# .add_resource(Data, '/data', endpoint='data')