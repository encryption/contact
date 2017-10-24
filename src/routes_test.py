import mock
import unittest
from routes import app, contact


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    @mock.patch('form.form.submit')
    def test_submit_without_data(self, mock):
        response = self.app.post(
            '/',
            headers={'Referer': 'http://google.com'}
        )

        self.assertEqual(response.location, 'http://google.com?success')
        self.assertEqual(mock.called, False)

    @mock.patch('form.form.submit')
    def test_submit_with_data(self, mock):

        response = self.app.post(
            '/',
            data='name=bob',
            headers={'Referer': 'http://google.com'},
            content_type='application/x-www-form-urlencoded',
        )

        self.assertEqual(mock.called, True)
        self.assertEqual(mock.call_args[0][0].get('name'), 'bob')
        self.assertEqual(response.location, 'http://google.com?success')


if __name__ == '__main__':
    unittest.main()
