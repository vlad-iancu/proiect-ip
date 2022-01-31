class CoffeeRecipe:
    def __init__(self, id: int = 0, name: str = "", preparation_time: float = 0, ingredients_with_quantities: list = []):
        self.id = id
        self.name = name
        self.preparation_time = preparation_time
        self.ingredients_with_quantities = ingredients_with_quantities

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "preparation_time": self.preparation_time,
            "ingredients_with_quantities": self.ingredients_with_quantities
        }
