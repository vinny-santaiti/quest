from flask.ext.testing import TestCase

from . import app, db


class BaseTestCase(TestCase):
    """A base test case for flask app"""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestIndexCase(BaseTestCase):
    
    def test_index():
        response = self.client.post(url_for('index'), data={'name': 'Mario'})
        self.assertEqual(result.status_code, 200) 
