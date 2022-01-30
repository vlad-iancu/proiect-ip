from os import remove
import unittest
import sqlite3

from src.services.IngredientService import IngredientService
from src.models.Ingredient import Ingredient
from src.config.Configuration import Configuration


class IngredientTests(unittest.TestCase):
    def setUp(self) -> None:
        conf = Configuration.getInstance()
        conn = sqlite3.connect(conf.db.file)
        cursor = conn.cursor()
        sql_schema = open("./schema.sql")
        cursor.executescript(sql_schema.read())
        sql_schema.close()

    def tearDown(self) -> None:
        conf = Configuration.getInstance()
        remove(conf.db.file)

    def testAddIngredient(self):
        # Arrange
        conf = Configuration.getInstance()
        ingredient: Ingredient = Ingredient()
        ingredient.name = "MyIngredient"
        ingredient.unit = "g"
        ingredient.available = 50

        # Act
        service: IngredientService = IngredientService()
        id = service.addIngredient(ingredient)

        # Assert
        conn = sqlite3.connect(conf.db.file)
        cursor = conn.execute("SELECT * FROM Ingredient WHERE id = ?", (id,))
        results = cursor.fetchall()
        self.assertNotEqual(len(results), 0)
        ingredientResult: Ingredient = Ingredient()
        ingredientResult.id = results[0][0]
        ingredientResult.name = results[0][1]
        ingredientResult.unit = results[0][2]
        ingredientResult.available = results[0][3]
        self.assertEqual(ingredient.name, ingredientResult.name)
        self.assertEqual(ingredient.available, ingredientResult.available)
        self.assertEqual(ingredient.unit, ingredientResult.unit)

    def testGetAllIngredients(self):
        # Arrange
        conf = Configuration.getInstance()
        conn = sqlite3.connect(conf.db.file)
        conn.execute("INSERT INTO Ingredient(name, available, measure_unit) VALUES(?,?,?)",
                     ("MyIngredient1", 100, "g"))
        conn.execute("INSERT INTO Ingredient(name, available, measure_unit) VALUES(?,?,?)",
                     ("MyIngredient2", 100, "g"))
        conn.commit()
        # Act
        service: IngredientService = IngredientService()
        data = service.getAllIngredients()

        # Assert
        self.assertEqual("MyIngredient1", data[0].name)
        self.assertEqual(100, data[0].available)
        self.assertEqual("g", data[0].unit)

        self.assertEqual("MyIngredient2", data[1].name)
        self.assertEqual(100, data[1].available)
        self.assertEqual("g", data[1].unit)

    def testGetIngredientById(self):
        # Arrange
        conf = Configuration.getInstance()
        conn = sqlite3.connect(conf.db.file)
        conn.execute("INSERT INTO Ingredient(name, available, measure_unit) VALUES(?,?,?)",
                     ("MyIngredient1", 100, "g"))
        conn.execute("INSERT INTO Ingredient(name, available, measure_unit) VALUES(?,?,?)",
                     ("MyIngredient2", 100, "g"))
        conn.commit()

        # Act
        service: IngredientService = IngredientService()
        data = service.getIngredientById(1)

        # Assert
        self.assertEqual("MyIngredient1", data.name)
        self.assertEqual(100, data.available)
        self.assertEqual("g", data.unit)

    def testDeleteIngredients(self):
        # Arrange
        conf = Configuration.getInstance()
        conn = sqlite3.connect(conf.db.file)
        conn.execute("INSERT INTO Ingredient(name, available, measure_unit) VALUES(?,?,?)",
                     ("MyIngredient1", 100, "g"))
        conn.execute("INSERT INTO Ingredient(name, available, measure_unit) VALUES(?,?,?)",
                     ("MyIngredient2", 100, "g"))
        conn.commit()

        # Act
        service: IngredientService = IngredientService()
        deletedId = service.deleteIngredient(1)

        # Assert
        self.assertEqual(1, deletedId)
        cursor = conn.execute("SELECT * FROM Ingredient")
        results = cursor.fetchall()
        if(len(results) == 2):
            self.assertTrue(False)
        ingredientResult: Ingredient = Ingredient()
        ingredientResult.id = results[0][0]
        ingredientResult.name = results[0][1]
        ingredientResult.unit = results[0][2]
        ingredientResult.available = results[0][3]
        self.assertEqual("MyIngredient2", ingredientResult.name)
        self.assertEqual(100, ingredientResult.available)
        self.assertEqual("g", ingredientResult.unit)

    def testUpdateIngredient(self):
        # Arrange
        conf = Configuration.getInstance()
        conn = sqlite3.connect(conf.db.file)
        conn.execute("INSERT INTO Ingredient(name, available, measure_unit) VALUES(?,?,?)",
                     ("MyIngredient1", 100, "g"))
        conn.execute("INSERT INTO Ingredient(name, available, measure_unit) VALUES(?,?,?)",
                     ("MyIngredient2", 100, "g"))
        conn.commit()

        # Act
        service: IngredientService = IngredientService()
        ingredient: Ingredient = Ingredient(1, "UpdatedIngredient", "g", 100)
        service.updateIngredient(ingredient)

        # Assert
        cursor = conn.execute("SELECT * FROM Ingredient WHERE id = ?", (1,))
        results = cursor.fetchall()
        ingredientResult: Ingredient = Ingredient()
        ingredientResult.id = results[0][0]
        ingredientResult.name = results[0][1]
        ingredientResult.unit = results[0][2]
        ingredientResult.available = results[0][3]
        self.assertEqual("UpdatedIngredient", ingredientResult.name)
        self.assertEqual(100, ingredientResult.available)
        self.assertEqual("g", ingredientResult.unit)
