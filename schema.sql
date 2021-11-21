CREATE TABLE Ingredient (
  id INTEGEREGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(255) NOT NULL,
  measure_unit VARCHAR(255) NOT NULL,
  available DECIMAL(10,5) NOT NULL
);

CREATE TABLE CoffeeRecipe (
  id INTEGEREGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE CoffeeRecipeIngredient (
  recipe_id INTEGER,
  ingredient_id INTEGER,
  quantity DECIMAL(10,5) NOT NULL,
  PRIMARY KEY (recipe_id, ingredient_id),
  FOREIGN KEY (recipe_id) REFERENCES CoffeeRecipe (id),
  FOREIGN KEY (ingredient_id) REFERENCES Ingredient (id)
);

CREATE TABLE CoffeePreparation (
  recipe_id INTEGER,
  started_at TIMESTAMP,
  finished_at TIMESTAMP,
  ingredients_json VARCHAR(255) NOT NULL,
  PRIMARY KEY (recipe_id, started_at),
  FOREIGN KEY (recipe_id) REFERENCES CoffeeRecipe (id)
);

CREATE TABLE Log (
  id INTEGEREGER PRIMARY KEY AUTOINCREMENT,
  type VARCHAR(255) NOT NULL,
  properties_json VARCHAR(255) NOT NULL,
  at TIMESTAMP NOT NULL
);