from datetime import datetime
from typing import List
from src.db import get_db
from src.models.CoffeePreparation import CoffeePreparation
from src.models.CoffeeRecipe import CoffeeRecipe


class CoffeePreparationRepository:

    def add(self, data: CoffeePreparation):
        db = get_db()

        db.execute(
            'INSERT INTO CoffeePreparation (recipe_id, started_at, finished_at, ingredients_with_quantities)'
            ' VALUES (?,?,?,?)',
            (data.recipe_id, data.started_at, data.finished_at, data.ingredients_with_quantities)
        )

        db.commit()

        row = db.execute(
            'SELECT * FROM CoffeePreparation'
            ' WHERE recipe_id = (?) AND started_at = (?)',
            (data.recipe_id, data.started_at)
        ).fetchone()

        coffeepreparation: CoffeePreparation = CoffeePreparation()
        coffeepreparation.recipe_id = row[0]
        coffeepreparation.started_at = row[1]
        coffeepreparation.finished_at = row[2]
        coffeepreparation.ingredients_with_quantities = row[3]

        return coffeepreparation

    def getAll(self):
        rows = get_db().execute(
            'SELECT * FROM coffeepreparation ORDER BY finished_at DESC').fetchall()

        if rows is None:
            return None

        coffeepreparations: List[CoffeePreparation] = []

        for row in rows:
            coffeepreparation: CoffeePreparation = CoffeePreparation()
            coffeepreparation.recipe_id = row[0]
            coffeepreparation.started_at = row[1]
            coffeepreparation.finished_at = row[2]
            coffeepreparation.ingredients_with_quantities = row[3]
            coffeepreparations.append(coffeepreparation)

        return coffeepreparations

    def getMostRecent(self):
        row = get_db().execute(
            'SELECT * FROM coffeepreparation ORDER BY finished_at DESC LIMIT 1').fetchone()

        if row is None:
            return None

        coffeepreparation: CoffeePreparation = CoffeePreparation()

        coffeepreparation.recipe_id = row[0]
        coffeepreparation.started_at = row[1]
        coffeepreparation.finished_at = row[2]
        coffeepreparation.ingredients_with_quantities = row[3]

        return coffeepreparation

    def getMostPrepared(self):
        row = get_db().execute(
            'SELECT recipe_id, COUNT(*) AS times_prepared'
            ' FROM coffeepreparation'
            ' GROUP BY recipe_id'
            ' ORDER BY times_prepared DESC'
            ' LIMIT 1'
        ).fetchone()

        if row is None:
            return None

        recipe_id = row[0]

        coffee_recipe = get_db().execute(
            'SELECT id, name, preparation_time'
            ' FROM coffeerecipe'
            ' WHERE id = (?)',
            (recipe_id,)).fetchone()

        recipe: CoffeeRecipe = CoffeeRecipe()
        recipe.id = coffee_recipe[0]
        recipe.name = coffee_recipe[1]
        recipe.preparation_time = coffee_recipe[2]

        return recipe
