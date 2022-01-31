from src.db import get_db


class CoffeePreparationRepository:

    def get_all(self):
        coffee_preparations = get_db().execute(
            'SELECT * FROM coffeepreparation ORDER BY finished_at DESC').fetchall()

        return coffee_preparations

    def get_most_recent(self):
        coffee_preparation = get_db().execute(
            'SELECT * FROM coffeepreparation ORDER BY finished_at DESC LIMIT 1').fetchone()

        return coffee_preparation

    def update_ingredients_by_name(self, ingredients, quantities):
        db = get_db()

        for i in range(len(ingredients)):
            ingredient_name = ingredients[i]
            quantity = quantities[i]

            db.execute(
                'UPDATE Ingredients '
                ' SET available = available - (?) '
                ' WHERE name = (?)',
                (quantity, ingredient_name)
            )

        db.commit()

        updated_ingredients = get_db().execute(
            'SELECT name, available'
            ' FROM ingredients'
            ' ORDER BY name'
        ).fetchall()

        return updated_ingredients

    def update_ingredients_by_id(self, ingredients, quantities):
        db = get_db()

        for i in range(len(ingredients)):
            ingredient_id = ingredients[i]
            quantity = quantities[i]

            db.execute(
                'UPDATE Ingredients '
                ' SET available = available - (?) '
                ' WHERE id = (?)',
                (quantity, ingredient_id)
            )

        db.commit()

        updated_ingredients = get_db().execute(
            'SELECT name, available'
            ' FROM ingredients'
            ' ORDER BY name'
        ).fetchall()

        return updated_ingredients

    def get_most_prepared(self):
        coffee_preparation = get_db().execute(
            'SELECT COUNT(*) AS times_prepared'
            ' FROM coffeepreparation'
            ' GROUP BY recipe_id'
            ' ORDER BY times_prepared DESC'
            ' LIMIT 1'
        ).fetchone()

        return coffee_preparation
