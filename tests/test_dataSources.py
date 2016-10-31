from base64 import b64encode
from unittest import TestCase


# -*- coding: utf-8 -*-
from app import create_app, db
from app.consts import APPLICATION_JSON
from app.models import Role, User


class TestDataSources(TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def get_api_headers(self, username, password):
        return{
            'Authorization': 'Basic' + b64encode((username + ':' + password).encode('utf-8')).decode('utf-8'),
            'Accept': APPLICATION_JSON,
            'Content-Type': APPLICATION_JSON
        }

    def test_token_auth(self):
        r = Role.query.filter_by(name='User').first()
        self.assertIsNotNone(r)
        u = User(email='sunlc@qkjr.com.cn', password='cat', confirmed=True, role=r)
        db.session.add(u)
        db.session.commit()
        pass

    def test_get(self):
        pass
