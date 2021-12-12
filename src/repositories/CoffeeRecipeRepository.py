from typing import List
from src.db import get_db
from src.models.CoffeeRecipe import CoffeeRecipe


class CoffeeRecipeRepository:

    def add(self, recipe: CoffeeRecipe):
        db = get_db()

        db.execute(
            'INSERT INTO CoffeeRecipe (name, preparation_time)'
            ' VALUES (?,?)',
            (recipe.name, recipe.preparation_time)
        )

        coffee_recipe_id = db.execute(
            'SELECT * FROM CoffeeRecipe'
            ' WHERE name = (?)',
            (recipe.name,)
        ).fetchone()[0]

        for coffee_recipe_ingredient in recipe.ingredients_with_quantities:
            db.execute(
                'INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity)'
                ' VALUES (?,?,?)',
                (int(coffee_recipe_id),
                 int(coffee_recipe_ingredient[0]),
                 int(coffee_recipe_ingredient[1]))
            )

        db.commit()

        added_recipe = db.execute(
            'SELECT * FROM CoffeeRecipe'
            ' WHERE name = (?)',
            (recipe.name,)
        ).fetchone()

        return added_recipe

    def getAll(self) -> List[CoffeeRecipe]:
        db = get_db()

        rows = db.execute("SELECT * FROM CoffeeRecipe ORDER BY id")

        results: List[CoffeeRecipe] = []

        for row in rows:
            recipe: CoffeeRecipe = CoffeeRecipe()
            recipe.id = row[0]
            recipe.name = row[1]
            recipe.preparation_time = row[2]
            results.append(recipe)

        return results

    def getRecipeIdByName(self, recipe_name):
        coffee_recipe_id = get_db().execute(
            'SELECT id'
            ' FROM CoffeeRecipe'
            ' WHERE name = (?)',
            (recipe_name)
        ).fetchone()[0]

        return coffee_recipe_id

    def getIngredientIdsByRecipeId(self, recipe_id):
        ingredients = get_db().execute(
            'SELECT id'
            ' FROM CoffeeRecipeIngredient'
            ' WHERE recipe_id = (?)',
            (recipe_id)
        ).fetchall()

        return ingredients

    def getAvailable(self):
        rows = get_db().execute(
            'SELECT * FROM coffeerecipe cri1, ' +
            '(SELECT recipe_id, count(*) as no_ingredients_total ' +
            'FROM coffeerecipeingredient cri JOIN ingredient i ' +
            'WHERE cri.ingredient_id = i.id GROUP BY cri.recipe_id) cri2,' +
            '(SELECT recipe_id, count(*) as no_ingredients_available ' +
            'FROM coffeerecipeingredient JOIN ingredient i ' +
            'WHERE ingredient_id = id AND quantity <= available ' +
            'GROUP BY recipe_id) cri3 ' +
            'WHERE cri1.id = cri2.recipe_id ' +
            'AND cri2.recipe_id = cri3.recipe_id ' +
            'AND cri2.no_ingredients_total = cri3.no_ingredients_available'
        ).fetchall()

        results: List[CoffeeRecipe] = []

        for row in rows:
            recipe: CoffeeRecipe = CoffeeRecipe()
            recipe.id = row[0]
            recipe.name = row[1]
            recipe.preparation_time = row[2]
            results.append(recipe)

        return results
