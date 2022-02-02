import json
import unittest
from src.main import app

from src.db import get_db


class IngredientControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = get_db()
        self.app.application.config.from_mapping(
            SECRET_KEY='dev',
        )

    def testGetAllIngredients(self):
        # When
        response = self.app.get('/ingredients/')

        # Then
        self.assertEqual('All ingredients successfully retrieved', response.json['status'])
        self.assertEqual(200, response.status_code)

    def testAddIngredient_Unauthenticated(self):
        # Given
        payload = {
            "name": "MyIngredient",
            "unit": "ml",
            "available": 50.0
        }

        with self.app:
            # When
            response = self.app.post('/ingredients/', data=payload)

        # Then
        self.assertEqual('User is not authenticated', response.json['status'])
        self.assertEqual(403, response.status_code)

    def testAddIngredient_Successful(self):
        # Given
        payload = {
            "username": "user",
            "password": "pass"
        }

        payload2 = {
            "name": "MyIngredient",
            "unit": "ml",
            "available": 50.0
        }

        # When
        with self.app:
            response1 = self.app.post('/auth/register', data=payload)
            response2 = self.app.post('/auth/login', data=payload)
            response3 = self.app.post('/ingredients/', data=json.dumps(payload2),
                                      content_type='application/json')

        # Then
        self.assertEqual('Ingredient successfully added', response3.json['status'])
        self.assertEqual(201, response3.status_code)

    def testUpdateIngredient(self):
        # Given
        payload = {
            "username": "user",
            "password": "pass"
        }

        payload2 = {
            "name": "MyIngredient",
            "unit": "ml",
            "available": 50.0
        }

        payload3 = {
            "name": "MyIngredient",
            "unit": "ml",
            "available": 60.0
        }

        # When
        with self.app:
            response1 = self.app.post('/auth/register', data=payload)
            response2 = self.app.post('/auth/login', data=payload)
            response3 = self.app.post('/ingredients/', data=json.dumps(payload2),
                                      content_type='application/json')
            response4 = self.app.put('/ingredients/0', data=json.dumps(payload3),
                                     content_type='application/json')

        # Then
        self.assertEqual('Ingredient successfully updated', response4.json['status'])

        updatedIngredient = {'available': 60.0, 'id': '0', 'name': 'MyIngredient', 'unit': 'ml'}
        self.assertEqual(updatedIngredient, response4.json['data']['ingredient'])
        self.assertEqual(200, response4.status_code)

    def testDeleteIngredient(self):
        # Given
        payload = {
            "username": "user",
            "password": "pass"
        }

        payload2 = {
            "name": "MyIngredient",
            "unit": "ml",
            "available": 50.0
        }

        # When
        with self.app:
            response1 = self.app.post('/auth/register', data=payload)
            response2 = self.app.post('/auth/login', data=payload)
            response3 = self.app.post('/ingredients/', data=json.dumps(payload2),
                                      content_type='application/json')
            response4 = self.app.delete('/ingredients/0')

        # Then
        self.assertEqual('Ingredient successfully deleted', response4.json['status'])
        self.assertEqual(200, response4.status_code)
