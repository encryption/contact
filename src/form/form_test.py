import unittest
import submission


class TestFormSubmission(unittest.TestCase):

    def test_submission(self):
        response = submission.submit('bob')
        self.assertEqual(response, 'hellobob')


if __name__ == "__main__":
    unittest.main()
