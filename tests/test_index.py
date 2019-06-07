from flask import url_for
import unittest

from . import app


class BaseTestCase(unittest.TestCase):
    """A base test case for flask app"""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass


class TestIndexCase(BaseTestCase):

    def test_index(self):
        response = self.client.post(url_for('index'), data={'name': 'Mario'})
        self.assertEqual(response.status_code, 200)
