from typing import List
from src.db import get_db
from src.models.CoffeeRecipe import CoffeeRecipe


class CoffeeRecipeRepository:

    def getById(self, id: int) -> CoffeeRecipe:
        row = get_db().execute("SELECT * FROM CoffeeRecipe WHERE id = ?", (id,)).fetchone()

        if(row is None):
            return None

        recipe: CoffeeRecipe = CoffeeRecipe()
        recipe.id = int(row[0])
        recipe.name = row[1]
        recipe.preparation_time = float(row[2])

        ingredientsWithQuantities = []
        results = get_db().execute(
            'SELECT i.name, cri.quantity '
            ' FROM CoffeeRecipeIngredient cri JOIN Ingredient i ON cri.ingredient_id = i.id'
            ' WHERE cri.recipe_id = ?', (id,)).fetchall()
        for result in results:
            ingredientsWithQuantities.append((result[0], float(result[1])))

        recipe.ingredients_with_quantities = ingredientsWithQuantities

        return recipe

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

        row = db.execute(
            'SELECT * FROM CoffeeRecipe'
            ' WHERE name = (?)',
            (recipe.name,)
        ).fetchone()

        recipe: CoffeeRecipe = CoffeeRecipe()
        recipe.id = int(row[0])
        recipe.name = row[1]
        recipe.preparation_time = float(row[2])

        ingredientsWithQuantities = []
        results = get_db().execute(
            'SELECT i.name, cri.quantity '
            ' FROM CoffeeRecipeIngredient cri JOIN Ingredient i ON cri.ingredient_id = i.id'
            ' WHERE cri.recipe_id = ?', (coffee_recipe_id,)).fetchall()
        for result in results:
            ingredientsWithQuantities.append((result[0], float(result[1])))

        recipe.ingredients_with_quantities = ingredientsWithQuantities

        return recipe

    def getAll(self) -> List[CoffeeRecipe]:
        rows = get_db().execute('SELECT * FROM CoffeeRecipe ORDER BY id').fetchall()

        recipes: List[CoffeeRecipe] = []

        for row in rows:
            recipe: CoffeeRecipe = CoffeeRecipe()
            recipe.id = int(row[0])
            recipe.name = row[1]
            recipe.preparation_time = float(row[2])

            ingredientsWithQuantities = []
            results = get_db().execute(
                'SELECT i.name, cri.quantity '
                ' FROM CoffeeRecipeIngredient cri JOIN Ingredient i ON cri.ingredient_id = i.id'
                ' WHERE cri.recipe_id = ?', (recipe.id,)).fetchall()
            for result in results:
                ingredientsWithQuantities.append((result[0], float(result[1])))

            recipe.ingredients_with_quantities = ingredientsWithQuantities
            recipes.append(recipe)

        return recipes

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

        available_recipes: List[CoffeeRecipe] = []

        for row in rows:
            recipe: CoffeeRecipe = CoffeeRecipe()
            recipe.id = row[0]
            recipe.name = row[1]
            recipe.preparation_time = row[2]

            ingredientsWithQuantities = []
            results = get_db().execute(
                'SELECT i.name, cri.quantity '
                ' FROM CoffeeRecipeIngredient cri JOIN Ingredient i ON cri.ingredient_id = i.id'
                ' WHERE cri.recipe_id = ?', (recipe.id,)).fetchall()
            for result in results:
                ingredientsWithQuantities.append((result[0], float(result[1])))

            recipe.ingredients_with_quantities = ingredientsWithQuantities

            available_recipes.append(recipe)

        return available_recipes
