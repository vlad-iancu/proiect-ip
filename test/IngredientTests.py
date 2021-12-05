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
    cursor = conn.execute("SELECT * FROM Ingredient WHERE id = ?",(id,))
    results = cursor.fetchall()
    if(len(results) == 0):
      self.assertTrue(False)
    ingredientResult: Ingredient = Ingredient()
    ingredientResult.id = results[0][0]
    ingredientResult.name = results[0][1]
    ingredientResult.unit = results[0][2]
    ingredientResult.available = results[0][3]
    self.assertEqual(ingredient.name, ingredientResult.name)
    self.assertEqual(ingredient.name, ingredientResult.name)
    self.assertEqual(ingredient.name, ingredientResult.name)
    self.assertEqual(ingredient.name, ingredientResult.name)

