CREATE TABLE User (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE Ingredient (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name TEXT NOT NULL,
  measure_unit TEXT NOT NULL,
  available REAL NOT NULL
);

CREATE TABLE CoffeeRecipe (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE CoffeeRecipeIngredient (
  recipe_id INTEGER,
  ingredient_id INTEGER,
  quantity REAL NOT NULL,
  PRIMARY KEY (recipe_id, ingredient_id)
);

CREATE TABLE CoffeePreparation (
  recipe_id INTEGER,
  started_at timestamp,
  finished_at timestamp,
  ingredients_json TEXT NOT NULL,
  PRIMARY KEY (recipe_id, started_at)
);

CREATE TABLE Log (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  type TEXT NOT NULL,
  properties_json TEXT NOT NULL,
  at timestamp NOT NULL
);

ALTER TABLE CoffeeRecipeIngredient ADD FOREIGN KEY (recipe_id) REFERENCES CoffeeRecipe (id);

ALTER TABLE CoffeeRecipeIngredient ADD FOREIGN KEY (ingredient_id) REFERENCES Ingredient (id);

ALTER TABLE CoffeePreparation ADD FOREIGN KEY (recipe_id) REFERENCES CoffeeRecipe (id);

