import unittest
from flask import url_for

from quest.app import app


class BaseTestCase(unittest.TestCase):
    """A base test case for flask app"""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass


class TestIndexCase(BaseTestCase):

    def test_index(self):
        response = self.app.get('/mario')
        self.assertEqual(response.status_code, 200)
