import unittest


from src.main import app

from src.db import get_db


class CoffeeRecipeControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = get_db()

    def testGetCoffeeRecipes(self):
        # When
        response = self.app.get('/coffeerecipes/')

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual('Coffee recipes successfully retrieved', response.json['status'])

    def testGetRecommendedCoffeeRecipes(self):
        # Given
        payload = {
            "current_time": "17:30",
            "temperature": "35"
        }
        # When
        response = self.app.get('/coffeerecipes/recommendations', data=payload)

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual('Coffee recommendations successfully retrieved', response.json['status'])
        self.assertEqual('Caramel Frappe', response.json['data']['recommendations'][0])
        self.assertEqual('Mocca', response.json['data']['recommendations'][1])

    def testGetAvailableCoffeeRecipes(self):
        # When
        response = self.app.get('/coffeerecipes/available')

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual('Available coffee recipes successfully retrieved', response.json['status'])
