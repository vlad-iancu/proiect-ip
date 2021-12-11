from src.db import get_db


class CoffeeRecipeRepository:

    def __init__(self) -> None:
        pass

    def get_all():
        coffee_recipes = get_db().execute('SELECT * FROM coffeerecipe ORDER BY name').fetchall()

        return coffee_recipes

    def get_available():
        available_coffees = get_db().execute(
            'SELECT cri1.name FROM coffeerecipe cri1, ' +
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

        return available_coffees
