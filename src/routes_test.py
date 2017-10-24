import os
from routes import app
import unittest


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_submit(self):
        response = self.app.post(
            '/',  headers={'Referer': 'http://google.com'})
        self.assertEqual(response.location, 'http://google.com?success')


if __name__ == '__main__':
    unittest.main()
