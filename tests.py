import unittest
from app import flask_app

class TestHome(unittest.TestCase):

    def test_get(self):
        app = flask_app.test_client()
        response = app.get('/')
        self.assertEqual(200, response.status_code)

if __name__ == '__main__':
    unittest.main()
