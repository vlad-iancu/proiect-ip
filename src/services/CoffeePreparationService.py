from datetime import datetime, timedelta
from typing import List
from src.models.CoffeePreparation import CoffeePreparation
from src.models.CoffeeRecipe import CoffeeRecipe
from src.repositories.CoffeePreparationRepository import CoffeePreparationRepository
from src.repositories.CoffeeRecipeRepository import CoffeeRecipeRepository
from src.repositories.IngredientRepository import IngredientRepository


class CoffeePreparationService:
    def __init__(self) -> None:
        self.coffeePreparationRepository = CoffeePreparationRepository()
        self.coffeeRecipeRepository = CoffeeRecipeRepository()
        self.ingredientRepository = IngredientRepository()

    def getAll(self) -> List[CoffeePreparation]:
        return self.coffeePreparationRepository.getAll()

    def getLastPrepared(self) -> CoffeePreparation:
        return self.coffeePreparationRepository.getMostRecent()

    def getMostPrepared(self) -> CoffeeRecipe:
        return self.coffeePreparationRepository.getMostPrepared()

    def prepareCoffeeCustom(self, recipeId: int, ingredients: List[str], quantities: List[int]) -> CoffeePreparation:
        recipe = self.coffeeRecipeRepository.getById(recipeId)

        if recipe is None:
            return None

        if (len(ingredients) != len(quantities)):
            return None

        for i in range(len(ingredients)):
            ingredient_name = ingredients[i]
            ingredient_quantity = quantities[i]
            self.ingredientRepository.decreaseQuantityByName(ingredient_quantity, ingredient_name)

        preparationTime = self.coffeeRecipeRepository.getById(recipeId).preparation_time

        coffeePreparation: CoffeePreparation = CoffeePreparation()
        coffeePreparation.recipe_id = recipeId

        currentTime = datetime.now()
        coffeePreparation.started_at = currentTime.strftime("%d/%m/%Y %H:%M:%S")
        coffeePreparation.finished_at = (
            currentTime + timedelta(minutes=preparationTime)).strftime("%d/%m/%Y %H:%M:%S")
        coffeePreparation.ingredients_with_quantities = str(
            [(ingredients[i], quantities[i]) for i in range(0, len(ingredients))]).strip('[]')

        result = self.coffeePreparationRepository.add(coffeePreparation)
        return result

    def prepareCoffeePremade(self, recipeId: int) -> CoffeePreparation:
        recipe = self.coffeeRecipeRepository.getById(recipeId)

        if not recipe:
            return None

        ingredients_with_quantities = list(map(list, zip(*recipe.ingredients_with_quantities)))
        ingredients = ingredients_with_quantities[0]
        quantities = ingredients_with_quantities[1]
        return CoffeePreparationService().prepareCoffeeCustom(recipeId, ingredients, quantities)
