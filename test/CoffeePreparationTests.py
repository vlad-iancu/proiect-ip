import sqlite3
import unittest

from src.config.Configuration import get_configuration
from src.services.CoffeePreparationService import CoffeePreparationService


class CoffeePreparationTests(unittest.TestCase):
    def setUp(self) -> None:
        conf = get_configuration()
        conn = sqlite3.connect(conf.db_file)
        cursor = conn.cursor()
        sql_schema = open("./schema.sql")
        cursor.executescript(sql_schema.read())
        sql_schema.close()

    def testGetAll(self):
        # Arrange
        conf = get_configuration()
        conn = sqlite3.connect(conf.db_file)
        conn.execute("INSERT INTO CoffeeRecipe (id, name, preparation_time) VALUES (?, ?,?)",
                     (1, 'Irish Cappuccino', 5.00))
        conn.execute("INSERT INTO CoffeePreparation (recipe_id, started_at, finished_at, ingredients_with_quantities) VALUES (?,?,?,?)",
                     (1, '25/06/2021 07:58:56', '25/06/2021 07:59:56', "('Milk', 100), ('Coffee', 50)"))
        conn.execute("INSERT INTO CoffeePreparation (recipe_id, started_at, finished_at, ingredients_with_quantities) VALUES (?,?,?,?)",
                     (2, '26/06/2021 07:58:56', '26/06/2021 07:59:56', "('Milk', 100), ('Coffee', 50)"))
        conn.commit()

        # Act
        service: CoffeePreparationService = CoffeePreparationService()
        data = service.getAll()

        # Assert
        self.assertEqual(len(data), 2)
        self.assertEqual(2, data[0].recipe_id)
        self.assertEqual('26/06/2021 07:58:56', data[0].started_at)
        self.assertEqual('26/06/2021 07:59:56', data[0].finished_at)
        self.assertEqual("('Milk', 100), ('Coffee', 50)", data[0].ingredients_with_quantities)

        self.assertEqual(1, data[1].recipe_id)
        self.assertEqual('25/06/2021 07:58:56', data[1].started_at)
        self.assertEqual('25/06/2021 07:59:56', data[1].finished_at)
        self.assertEqual("('Milk', 100), ('Coffee', 50)", data[1].ingredients_with_quantities)

    def testGetAll_Empty(self):
        # Arrange
        conf = get_configuration()
        conn = sqlite3.connect(conf.db_file)

        # Act
        service: CoffeePreparationService = CoffeePreparationService()
        data = service.getAll()

        # Assert
        self.assertEqual(0, len(data))

    def testGetLastPrepared(self):
        # Arrange
        conf = get_configuration()
        conn = sqlite3.connect(conf.db_file)
        conn.execute("INSERT INTO CoffeeRecipe (id, name, preparation_time) VALUES (?, ?,?)",
                     (1, 'Irish Cappuccino', 5.00))
        conn.execute("INSERT INTO CoffeePreparation (recipe_id, started_at, finished_at, ingredients_with_quantities) VALUES (?,?,?,?)",
                     (1, '25/06/2021 07:58:56', '25/06/2021 07:59:56', "('Milk', 100), ('Coffee', 50)"))
        conn.execute("INSERT INTO CoffeePreparation (recipe_id, started_at, finished_at, ingredients_with_quantities) VALUES (?,?,?,?)",
                     (1, '26/06/2021 07:58:56', '26/06/2021 07:59:56', "('Milk', 100), ('Coffee', 50)"))
        conn.execute("INSERT INTO CoffeePreparation (recipe_id, started_at, finished_at, ingredients_with_quantities) VALUES (?,?,?,?)",
                     (1, '26/06/2021 17:58:56', '26/06/2021 17:59:56', "('Milk', 100), ('Coffee', 50)"))
        conn.commit()

        # Act
        service: CoffeePreparationService = CoffeePreparationService()
        data = service.getLastPrepared()

        # Assert
        self.assertIsNotNone(data)
        self.assertEqual(1, data.recipe_id)
        self.assertEqual('26/06/2021 17:58:56', data.started_at)
        self.assertEqual('26/06/2021 17:59:56', data.finished_at)
        self.assertEqual("('Milk', 100), ('Coffee', 50)", data.ingredients_with_quantities)

    def testGetMostPrepared(self):
        # Arrange
        conf = get_configuration()
        conn = sqlite3.connect(conf.db_file)
        conn.execute("INSERT INTO CoffeeRecipe (id, name, preparation_time) VALUES (?,?,?)",
                     (1, 'Irish Cappuccino', 5.00))
        conn.execute("INSERT INTO CoffeeRecipe (id, name, preparation_time) VALUES (?,?,?)",
                     (2, 'Hot Chocolate', 3.5))

        conn.execute("INSERT INTO CoffeePreparation (recipe_id, started_at, finished_at, ingredients_with_quantities) VALUES (?,?,?,?)",
                     (1, '25/06/2021 07:58:56', '25/06/2021 07:59:56', "('Milk', 100), ('Coffee', 50)"))
        conn.execute("INSERT INTO CoffeePreparation (recipe_id, started_at, finished_at, ingredients_with_quantities) VALUES (?,?,?,?)",
                     (2, '26/06/2021 07:58:56', '26/06/2021 07:59:56', "('Milk', 100), ('Coffee', 50)"))
        conn.execute("INSERT INTO CoffeePreparation (recipe_id, started_at, finished_at, ingredients_with_quantities) VALUES (?,?,?,?)",
                     (2, '26/06/2021 17:58:56', '26/06/2021 17:59:56', "('Milk', 100), ('Coffee', 50)"))
        conn.commit()

        # Act
        service: CoffeePreparationService = CoffeePreparationService()
        data = service.getMostPrepared()

        # Assert
        self.assertIsNotNone(data)
        self.assertEqual(2, data.id)
        self.assertEqual('Hot Chocolate', data.name)
        self.assertEqual(3.5, data.preparation_time)

    def testPrepareCoffeeCustom(self):
        # Arrange
        conf = get_configuration()
        conn = sqlite3.connect(conf.db_file)
        recipeId = 1
        ingredients = ['Milk', 'Coffee']
        quantities = [50, 100]

        # Act
        conn.execute("INSERT INTO CoffeeRecipe (id, name, preparation_time) VALUES (?,?,?)",
                     (1, 'Irish Cappuccino', 5.00))
        conn.execute("INSERT INTO Ingredient(id, name, available, measure_unit) VALUES(?,?,?,?)",
                     (1, "Milk", 100, "g"))
        conn.execute("INSERT INTO Ingredient(id, name, available, measure_unit) VALUES(?,?,?,?)",
                     (2, "Coffee", 200, "ml"))
        conn.execute("INSERT INTO CoffeePreparation (recipe_id, started_at, finished_at, ingredients_with_quantities) VALUES (?,?,?,?)",
                     (1, '26/06/2021 17:58:56', '26/06/2021 17:59:56', "('Milk', 100), ('Coffee', 50)"))
        conn.commit()

        service: CoffeePreparationService = CoffeePreparationService()
        data = service.prepareCoffeeCustom(recipeId, ingredients, quantities)

        # Assert
        result = conn.execute("SELECT * FROM CoffeePreparation ORDER BY started_at ASC").fetchall()
        self.assertIsNotNone(data)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][0], data.recipe_id)
        self.assertEqual(result[0][1], data.started_at)
        self.assertEqual(result[0][2], data.finished_at)
        self.assertEqual(result[0][3], data.ingredients_with_quantities)

    def testPrepareCoffeePremade(self):
        # Arrange
        conf = get_configuration()
        conn = sqlite3.connect(conf.db_file)

        # Act
        conn.execute("INSERT INTO CoffeeRecipe (id, name, preparation_time) VALUES (?,?,?)",
                     (1, 'Irish Cappuccino', 5.00))
        conn.execute("INSERT INTO Ingredient(id, name, available, measure_unit) VALUES(?,?,?,?)",
                     (1, "MyIngredient1", 100, "g"))
        conn.execute("INSERT INTO Ingredient(id, name, available, measure_unit) VALUES(?,?,?,?)",
                     (2, "MyIngredient2", 200, "ml"))

        conn.execute("INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (?,?,?)",
                     (1, 1, 50))
        conn.execute("INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (?,?,?)",
                     (1, 2, 70))
        conn.commit()

        service: CoffeePreparationService = CoffeePreparationService()
        data = service.prepareCoffeePremade(1)

        self.assertEqual(1, data.recipe_id)
        self.assertEqual("('MyIngredient1', 50.0), ('MyIngredient2', 70.0)",
                         data.ingredients_with_quantities)
