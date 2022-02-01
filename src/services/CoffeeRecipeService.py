from typing import List
from src.models.CoffeeRecipe import CoffeeRecipe
from src.repositories.CoffeeRecipeRepository import CoffeeRecipeRepository


class CoffeeRecipeService:
    def __init__(self):
        self.coffeeRecipeRepository = CoffeeRecipeRepository()

    def getAll(self) -> List[CoffeeRecipe]:
        return self.coffeeRecipeRepository.getAll()

    def getById(self, id: int) -> CoffeeRecipe:
        return self.coffeeRecipeRepository.getById(id)

    def getAvailable(self) -> List[CoffeeRecipe]:
        return self.coffeeRecipeRepository.getAvailable()

    def add(self, recipe: CoffeeRecipe) -> CoffeeRecipe:
        return self.coffeeRecipeRepository.add(recipe)

    def getRecommendations(self, current_time: str, temperature: str) -> List[str]:
        recommendations = None

        if ('06:00' <= current_time <= '12:00'):
            recommendations = ['Short Espresso', 'Long Espresso']
        if ('12:00' < current_time <= '17:00'):
            recommendations = ['Long Espresso', 'Cappuccino']
        if ('17:00' < current_time <= '21:00'):
            if (int(temperature) < 5):
                recommendations = ['Hot Chocolate', 'Irish Coffee']
            else:
                recommendations = ['Caramel Frappe', 'Mocca']
        if ('21:00' < current_time <= '23:59' or '00:00' <= current_time < '06:00'):
            if (int(temperature) < 5):
                recommendations = ['Hot Chocolate']
            else:
                recommendations = ['Caramel Frappe']

        return recommendations
