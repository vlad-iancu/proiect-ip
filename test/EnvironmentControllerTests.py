import unittest
from src.main import app

from src.db import get_db


class EnvironmentControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = get_db()

    def testGetTemperature(self):
        # When
        response = self.app.get('/environment/temperature')

        # Then
        self.assertEqual('Temperature succesfully retrieved', response.json['status'])
        self.assertEqual(200, response.status_code)

    def testGetCurrentTime(self):
        # When
        response = self.app.get('/environment/currenttime')

        # Then
        self.assertEqual('Current time successfully retrieved', response.json['status'])
        self.assertEqual(200, response.status_code)

    def testSetTemperature(self):
        # Given
        payload = {
            "temp": "35"
        }

        # When
        response = self.app.post('/environment/temperature', data=payload)

        # Then
        self.assertEqual('Temperature succesfully recorded', response.json['status'])
        self.assertEqual(201, response.status_code)
