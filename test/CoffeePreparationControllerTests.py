import unittest
from src.config.Configuration import get_configuration


from src.main import app

from src.db import get_db


class CoffeePreparationControllerTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.application.config.from_mapping(SECRET_KEY='testsecret',)
        self.db = get_db()

    def testGetAllPreparedCoffees(self):
        # When
        response = self.app.get('/coffeepreparations/')

        # Then
        self.assertEqual('All coffee preparations successfully retrieved', response.json['status'])
        self.assertEqual(200, response.status_code)

    def testGetLastPreparedCoffee(self):
        # When
        response = self.app.get('/coffeepreparations/last')

        # Then
        self.assertEqual(200, response.status_code)
        self.assertEqual('Last prepared coffee successfully retrieved', response.json['status'])
        self.assertEqual('No coffee has been prepared yet',
                         response.json['data']['last_prepared_coffee'])
