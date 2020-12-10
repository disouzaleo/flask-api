import unittest
from app import flask_app

class TestHome(unittest.TestCase):
    """This class introduces API test case"""

    def setUp(self):
        self.client = flask_app.test_client

    def test_get(self):
        response = self.client().get('/')
        self.assertEqual(200, response.status_code)

    def test_content_type(self):
        response = self.client().get('/')
        self.assertIn('text/html', response.content_type)

    def test_error_404(self):
        response = self.client().get('/error')
        self.assertEqual(404, response.status_code)

if __name__ == '__main__':
    unittest.main()
