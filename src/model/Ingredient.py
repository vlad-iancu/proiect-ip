

class Ingredient:
  def __init__(self, id: int = 0, name: str = "", unit: str = "", available: float = -1):
    self.id = id
    self.name = name
    self.unit = unit
    self.available = available