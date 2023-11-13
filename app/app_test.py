"""We need to do unit test"""
import unittest

from app import app


"""My very importatn app test"""
class TestApp(unittest.TestCase):

    def __init__(self, arg):
        self.client=""


    def setUp(self):
        self.client = app.test_client()


    def test_hello_world(self):
        """Testing hello world"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")


if __name__ == "__main__":
    unittest.main()
