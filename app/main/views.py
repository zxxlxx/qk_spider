# -*- coding: utf-8 -*-

from datetime import datetime
from flask import render_template, session, redirect, url_for


from . import main


@main.route('/test')
def test():
    return 'OK!'
