from unittest import TestCase

from app.datasource.query import Query


class TestQuery(TestCase):
    query = Query()
    
    def test_query(self):
        self.query.query(user_name_cn='孙立超', mobile_num='15829551989', personal_id='210114198701251232', card_id='610527199005154925')
