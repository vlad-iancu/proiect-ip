from src.repositories.IngredientRepository import IngredientRepository
from src.models.Ingredient import Ingredient
from typing import List

class IngredientService:
  def __init__(self):
    self.repo = IngredientRepository()
  
  def addIngredient(self, ingredient: Ingredient) -> int:
    return self.repo.add(ingredient)

  def getIngredientById(self, id) -> Ingredient:
    return self.repo.getById() 

  def getAllIngredients(self) -> List[Ingredient]:
    return self.repo.getAll()