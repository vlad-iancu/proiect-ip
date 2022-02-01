import unittest
from src.main import app

from src.db import get_db


class AuthControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = get_db()

    def testRegisterSuccessful(self):
        # Given
        payload = {
            "username": "username",
            "password": "password"
        }

        # When
        response = self.app.post('/auth/register', data=payload)

        # Then
        self.assertEqual('user registered succesfully', response.json['status'])
        self.assertEqual(200, response.status_code)

    def testRegisterUsernameRequired(self):
        # Given
        payload = {
            "username": "",
            "password": "password"
        }

        # When
        response = self.app.post('/auth/register', data=payload)

        # Then
        self.assertEqual('Username is required.', response.json['status'])
        self.assertEqual(403, response.status_code)

    def testRegisterPasswordRequired(self):
        # Given
        payload = {
            "username": "user",
            "password": ""
        }

        # When
        response = self.app.post('/auth/register', data=payload)

        # Then
        self.assertEqual('Password is required.', response.json['status'])
        self.assertEqual(403, response.status_code)
