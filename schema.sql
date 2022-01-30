DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Ingredient;
DROP TABLE IF EXISTS CoffeePreparation;
DROP TABLE IF EXISTS CoffeeRecipe;
DROP TABLE IF EXISTS CoffeeRecipeIngredient;
DROP TABLE IF EXISTS Log;

CREATE TABLE User (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE Ingredient (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  measure_unit TEXT NOT NULL,
  available REAL NOT NULL
);

CREATE TABLE CoffeeRecipe (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  preparation_time REAL
);

CREATE TABLE CoffeeRecipeIngredient (
  recipe_id INTEGER,
  ingredient_id INTEGER,
  quantity REAL NOT NULL,
  PRIMARY KEY (recipe_id, ingredient_id),
  FOREIGN KEY (ingredient_id) REFERENCES Ingredient (id),
  FOREIGN KEY (recipe_id) REFERENCES CoffeeRecipe (id)
);

CREATE TABLE CoffeePreparation (
  recipe_id INTEGER,
  started_at TEXT,
  finished_at TEXT,
  ingredients_json TEXT NOT NULL,
  PRIMARY KEY (recipe_id, started_at),
  FOREIGN KEY (recipe_id) REFERENCES CoffeeRecipe (id)
);

CREATE TABLE Log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  type TEXT NOT NULL,
  properties_json TEXT NOT NULL,
  at TEXT NOT NULL
);
