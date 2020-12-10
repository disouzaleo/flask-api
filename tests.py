import unittest
from app import flask_app

class TestHome(unittest.TestCase):

    def setUp(self):
        app = flask_app.test_client()
        self.response = app.get('/')

    def test_get(self):
        self.assertEqual(200, response.status_code)

    def test_content_type(self):
        self.assertIn('text/html', response.content_type)

if __name__ == '__main__':
    unittest.main()
