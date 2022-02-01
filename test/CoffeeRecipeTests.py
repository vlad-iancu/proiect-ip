import unittest
import sqlite3

from src.config.Configuration import get_configuration
from src.models.CoffeeRecipe import CoffeeRecipe
from src.models.Ingredient import Ingredient
from src.repositories.CoffeeRecipeRepository import CoffeeRecipeRepository
from src.services.CoffeeRecipeService import CoffeeRecipeService
from src.services.IngredientService import IngredientService


class CoffeeRecipeTests(unittest.TestCase):
    def setUp(self) -> None:
        conf = get_configuration()
        conn = sqlite3.connect(conf.db_file)
        cursor = conn.cursor()
        clear_schema = open('./clear.sql')
        sql_schema = open("./schema.sql")
        cursor.executescript(clear_schema.read())
        cursor.executescript(sql_schema.read())
        sql_schema.close()
        clear_schema.close()
        conn.close()

    def testGetById(self):
        # Arrange
        conf = get_configuration()
        conn = sqlite3.connect(conf.db_file)
        conn.execute("INSERT INTO CoffeeRecipe (id, name, preparation_time) VALUES (?, ?,?)",
                     (200, 'Irish Cappuccino', 5.00))
        conn.commit()

        # Act
        service: CoffeeRecipeService = CoffeeRecipeService()
        data1 = service.getById(200)
        data2 = service.getById(5)

        # Assert
        self.assertIsNotNone(data1)
        self.assertEqual('Irish Cappuccino', data1.name)
        self.assertEqual(5.00, data1.preparation_time)
        self.assertIsNone(data2)

    def testGetAll(self):
        # Arrange
        conf = get_configuration()
        conn = sqlite3.connect(conf.db_file)
        conn.execute("INSERT INTO CoffeeRecipe (name, preparation_time) VALUES (?,?)",
                     ('Irish Cappuccino', 5.00))
        conn.execute("INSERT INTO CoffeeRecipe (name, preparation_time) VALUES (?,?)",
                     ('Hot Chocolate', 3.5))
        conn.execute("INSERT INTO CoffeeRecipe (name, preparation_time) VALUES (?,?)",
                     ('Short Espresso', 1))
        conn.commit()

        # Act
        service: CoffeeRecipeService = CoffeeRecipeService()
        data = service.getAll()

        # Assert
        self.assertEqual(len(data), 3)
        self.assertEqual('Irish Cappuccino', data[0].name)
        self.assertEqual(5.00, data[0].preparation_time)

        self.assertEqual('Hot Chocolate', data[1].name)
        self.assertEqual(3.5, data[1].preparation_time)

        self.assertEqual('Short Espresso', data[2].name)
        self.assertEqual(1, data[2].preparation_time)

    def testAddRecipe(self):
        # Arrange
        conf = get_configuration()

        ingredientOne: Ingredient = Ingredient()
        ingredientOne.name = "Ingredient 1"
        ingredientOne.unit = "g"
        ingredientOne.available = 50

        ingredientTwo: Ingredient = Ingredient()
        ingredientTwo.name = "Ingredient 2"
        ingredientTwo.unit = "ml"
        ingredientTwo.available = 100

        recipe: CoffeeRecipe = CoffeeRecipe()
        recipe.name = "Recipe 1"
        recipe.preparation_time = 5.5

        # Act
        recipeService: CoffeeRecipeService = CoffeeRecipeService()
        ingredientService: IngredientService = IngredientService()

        ingredientOneId = ingredientService.addIngredient(ingredientOne)
        ingredientTwoId = ingredientService.addIngredient(ingredientTwo)

        recipe.ingredients_with_quantities = [(ingredientOneId, 30.0), (ingredientTwoId, 70.0)]
        recipeId = recipeService.add(recipe).id
        print(recipeId)

        # Assert
        conn = sqlite3.connect(conf.db_file)
        cursor = conn.execute("SELECT * FROM CoffeeRecipe WHERE id = (?)", (recipeId,))
        results = cursor.fetchall()
        self.assertEqual(len(results), 1)
        recipeResult: CoffeeRecipe = CoffeeRecipe()
        recipeResult.id = results[0][0]
        recipeResult.name = results[0][1]
        recipeResult.preparation_time = results[0][2]

        cursor = conn.execute(
            "SELECT ingredient_id, quantity FROM CoffeeRecipeIngredient WHERE recipe_id = (?)", (recipeId,))
        results = cursor.fetchall()
        recipeResult.ingredients_with_quantities = results
        self.assertEqual(recipe.name, recipeResult.name)
        self.assertEqual(recipe.preparation_time, recipeResult.preparation_time)
        self.assertEqual(recipe.ingredients_with_quantities,
                         recipeResult.ingredients_with_quantities)

    def testGetRecommendations(self):
        conf = get_configuration()
        conn = sqlite3.connect(conf.db_file)
        conn.execute("INSERT INTO CoffeeRecipe (name) VALUES (?)", ('Irish Cappucino',))
        conn.execute("INSERT INTO CoffeeRecipe (name) VALUES (?)", ('Hot Chocolate',))
        conn.execute("INSERT INTO CoffeeRecipe (name) VALUES (?)", ('Short Espresso',))
        conn.execute("INSERT INTO CoffeeRecipe (name) VALUES (?)", ('Long Espresso',))

        # Act
        service: CoffeeRecipeService = CoffeeRecipeService()
        recommendationOne = service.getRecommendations('07:00', '30')
        recommendationTwo = service.getRecommendations('23:00', '-10')

        # Assert
        self.assertEqual(len(recommendationOne), 2)
        self.assertEqual(set(recommendationOne), set(['Long Espresso', 'Short Espresso']))
        self.assertEqual(len(recommendationTwo), 1)
        self.assertEqual(recommendationTwo, ['Hot Chocolate'])

    def testGetAvailable_NonEmptyList(self):
        conf = get_configuration()
        conn = sqlite3.connect(conf.db_file)
        conn.execute("INSERT INTO CoffeeRecipe (id, name) VALUES (?,?)", (1, 'Irish Cappucino',))
        conn.execute("INSERT INTO CoffeeRecipe (id, name) VALUES (?,?)", (2, 'Hot Chocolate',))

        conn.execute("INSERT INTO Ingredient(id, name, measure_unit, available) VALUES(?,?,?,?)",
                     (1, 'coffee', 'gr', 400))
        conn.execute("INSERT INTO Ingredient(id, name, measure_unit, available) VALUES(?,?,?,?)",
                     (2, 'milk', 'ml', 100))

        conn.execute(
            "INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (?,?,?)", (1, 1, 50))
        conn.execute(
            "INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (?,?,?)", (1, 2, 150))

        conn.execute(
            "INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (?,?,?)", (2, 1, 50))
        conn.execute(
            "INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (?,?,?)", (2, 2, 50))
        conn.commit()

        # Act
        service: CoffeeRecipeService = CoffeeRecipeService()
        available = service.getAvailable()

        # Assert
        self.assertEqual(len(available), 1)
        self.assertEqual('Hot Chocolate', available[0].name)

    def testGetAvailable_EmptyList(self):
        conf = get_configuration()
        conn = sqlite3.connect(conf.db_file)
        conn.execute("INSERT INTO CoffeeRecipe (id, name) VALUES (?,?)", (1, 'Irish Cappucino',))
        conn.execute("INSERT INTO CoffeeRecipe (id, name) VALUES (?,?)", (2, 'Hot Chocolate',))

        conn.execute("INSERT INTO Ingredient(id, name, measure_unit, available) VALUES(?,?,?,?)",
                     (1, 'coffee', 'gr', 400))
        conn.execute("INSERT INTO Ingredient(id, name, measure_unit, available) VALUES(?,?,?,?)",
                     (2, 'milk', 'ml', 100))

        conn.execute(
            "INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (?,?,?)", (1, 1, 50))
        conn.execute(
            "INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (?,?,?)", (1, 2, 150))

        conn.execute(
            "INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (?,?,?)", (2, 1, 50))
        conn.execute(
            "INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (?,?,?)", (2, 2, 101))
        conn.commit()

        # Act
        service: CoffeeRecipeService = CoffeeRecipeService()
        available = service.getAvailable()

        # Assert
        self.assertEqual(len(available), 0)
