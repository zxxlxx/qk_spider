# -*- coding: utf-8 -*-
import json
from datetime import time, datetime

from flask import redirect, request, jsonify

from app.api_1_0.errors import bad_request
from app.api_1_0.models import InnerResult
from app.datasource import ds
from flask_login import current_user, login_user, login_required
from app.datasource.query import Query
from flask_restful import reqparse, Resource
from app import api, db
from ..datasource.query import Query


class DataSources(Resource):
    """
    Restful for query
    """
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided', location='json')
        super(DataSources, self).__init__()

    def get(self):
        args = request.args.to_dict()
        have_result = InnerResult.query.filter_by(condition=str(args)).first()
        if have_result is not None:
            return have_result.result

        query = Query()
        result = query.query(**args)
        inner_result = InnerResult(condition=str(args), result=result, received_time=datetime.now())
        db.session.add(inner_result)
        db.session.commit()
        return result

api.add_resource(DataSources, '/data', endpoint='data')

