from src.repositories.CoffeePreparationRepository import CoffeePreparationRepository
from src.repositories.CoffeeRecipeRepository import CoffeeRecipeRepository


class CoffeePreparationService:
    def __init__(self) -> None:
        self.coffeePreparationRepository = CoffeePreparationRepository()
        self.coffeeRecipeRepository = CoffeeRecipeRepository()

    def get_all_coffee_preparations(self):
        coffee_preparations = self.coffeePreparationRepository.getAll()

        data = []
        for coffee_preparation in coffee_preparations:
            data.append(list(coffee_preparation))

        return data

    def get_last_coffee_preparation(self):
        coffee_preparation = self.coffeePreparationRepository.get_most_recent()

        data = list(coffee_preparation)

        return data

    def get_most_prepared_coffee(self):
        coffee_preparation = self.coffeePreparationRepository.get_most_prepared()

        data = list(coffee_preparation)

        return data

    def prepare_coffee_custom(self, ingredients, quantities):
        updated_ingredients = self.coffeePreparationRepository.update_ingredients_by_name(
            ingredients, quantities)

        data = list(updated_ingredients)

        return data

    def prepare_coffee_premade(self, recipe_name):
        recipe_id = self.coffeeRecipeRepository.getRecipeIdByName(recipe_name)

        if not recipe_id:
            return None

        ingredients = self.coffeeRecipeRepository.getIngredientIdsByRecipeId(recipe_id)
        quantities = self.coffeeRecipeRepository.getIngredientQuantitiesByRecipeId(recipe_id)

        updated_ingredients = self.coffeePreparationRepository.update_ingredients_by_id(
            ingredients, quantities)

        data = list(updated_ingredients)

        return data
