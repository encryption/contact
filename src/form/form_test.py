import unittest
import form


class TestFormSubmission(unittest.TestCase):

    def test_submit(self):
        response = form.submit('bob')
        self.assertEqual(response, True)


if __name__ == "__main__":
    unittest.main()
