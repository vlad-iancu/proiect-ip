import unittest
from src.main import app

from src.db import get_db


class AuthControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = get_db()
        self.app.application.config.from_mapping(
            SECRET_KEY='dev',
        )

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

    def testLoginUser(self):
        # Given
        payload = {
            "username": "user",
            "password": "pass"
        }

        # When
        with self.app:
            response1 = self.app.post('/auth/register', data=payload)
            response2 = self.app.post('/auth/login', data=payload)

        # Then
        self.assertEqual('user logged in succesfully', response2.json['status'])
        self.assertEqual(200, response2.status_code)

    def testRegisterAlreadyExists(self):
        # Given
        payload = {
            "username": "user",
            "password": "pass"
        }

        # When
        with self.app:
            response1 = self.app.post('/auth/register', data=payload)
            response2 = self.app.post('/auth/register', data=payload)

        # Then
        self.assertEqual('User user is already registered.', response2.json['status'])
        self.assertEqual(403, response2.status_code)

    def testLoginUsernameDoesntExists(self):
        # Given
        payload = {
            "username": "user",
            "password": "pass"
        }

        payload2 = {
            "username": "user2",
            "password": "pass"
        }

        # When
        with self.app:
            response1 = self.app.post('/auth/register', data=payload)
            response2 = self.app.post('/auth/login', data=payload2)

        # Then
        self.assertEqual('Username not found', response2.json['status'])
        self.assertEqual(403, response2.status_code)

    def testLoginIncorrectPassword(self):
        # Given
        payload = {
            "username": "user",
            "password": "pass"
        }

        payload2 = {
            "username": "user",
            "password": "passpass"
        }

        # When
        with self.app:
            response1 = self.app.post('/auth/register', data=payload)
            response2 = self.app.post('/auth/login', data=payload2)

        # Then
        self.assertEqual('Password is incorrect', response2.json['status'])
        self.assertEqual(403, response2.status_code)

    def testLogout(self):
        payload = {
            "username": "user",
            "password": "pass"
        }

        # When
        with self.app:
            response1 = self.app.post('/auth/register', data=payload)
            response2 = self.app.post('/auth/login', data=payload)
            response3 = self.app.get('/auth/logout')

        # Then
        self.assertEqual('user logged out succesfully', response3.json['status'])
        self.assertEqual(200, response2.status_code)
