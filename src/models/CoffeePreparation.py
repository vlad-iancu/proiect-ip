class CoffeePreparation:
    def __init__(self, recipe_id: int = 0, started_at: str = "", finished_at: float = 0, ingredients_with_quantities: str = ''):
        self.recipe_id = recipe_id
        self.started_at = started_at
        self.finished_at = finished_at
        self.ingredients_with_quantities = ingredients_with_quantities

    def serialize(self):
        return {
            "recipe_id": self.recipe_id,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "ingredients_with_quantities": self.ingredients_with_quantities
        }
