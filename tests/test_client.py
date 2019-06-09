import unittest
from tornapi import TornAPI


class TestTornAPI(unittest.TestCase):

    def setUp(self):
        self.api = TornAPI('fake-api-key')

    def test_get_user(self):
        # Mock the request and response here
        pass

    def test_get_city(self):
        # Mock the request and response here
        pass

    def test_error_handling(self):
        # Mock the request to return an error and test error handling
        pass


if __name__ == '__main__':
    unittest.main()
