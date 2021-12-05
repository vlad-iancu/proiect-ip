from src.repositories.CoffeeRecipeRepository import CoffeeRecipeRepository


class CoffeeRecipeService:
    def __init__(self) -> None:
        self.coffeeRecipeRepository = CoffeeRecipeRepository()
        pass

    def get_all_coffee_recipes(self):
        coffee_recipes = self.coffeeRecipeRepository.get_all()

        data = []
        for coffee_recipe in coffee_recipes:
            data.append([x for x in coffee_recipe])

        return data

    def get_available_coffee_recipes(self):
        available_coffees = self.coffeeRecipeRepository.get_available()

        data = []
        for available_coffee in available_coffees:
            data.append([x for x in available_coffee])

        return data
