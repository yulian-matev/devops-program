"""We need to do unit test"""
import unittest

from app import app



class TestApp(unittest.TestCase):
    """My very importatn TestApp"""

    def setUp(self):
        self.client = app.test_client()


    def test_hello_world(self):
        """Testing hello world"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, World!")


if __name__ == "__main__":
    #suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestApp)
    #unittest.TextTestRunner().run(suite)
    unittest.main()
