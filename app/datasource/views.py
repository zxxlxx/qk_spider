# -*- coding: utf-8 -*-

from flask import redirect, request
from . import ds
from flask_login import current_user, login_user, login_required
from .query import Query


@ds.route('/query', methods=['GET'])
@login_required
def query():
    
    query = Query()
    query.q


