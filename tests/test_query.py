from unittest import TestCase

from app.datasource.query import Query


class TestQuery(TestCase):
    query = Query()
    
    def test_query(self):
        self.query.query(name='孙立超', personal_id='210114198701251232', card_id='610527199005154925')
