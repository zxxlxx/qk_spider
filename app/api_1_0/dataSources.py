# -*- coding: utf-8 -*-

from flask import redirect, request, jsonify
from app.datasource import ds
from flask_login import current_user, login_user, login_required
from app.datasource.query import Query
from flask_restful import reqparse, Resource
from app import api
from ..datasource.query import Query

class DataSources(Resource):
    """
    Restful for query
    """
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided', location='json')
        self.reqparse.add_argument('description', type=str, default="", location='json')
        super(DataSources, self).__init__()

    def get(self):
        query = Query()
        result = self.query()
        return {}

api.add_resource(DataSources, '/data', endpoint='data')

