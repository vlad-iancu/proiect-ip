import unittest
from src.main import app

from src.db import get_db


class MainTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = get_db()

    def testRootEndpoints(self):
        landing = self.app.get("/")
        html = landing.data.decode()

        assert 'Hello, World!' in html
        assert landing.status_code == 200
