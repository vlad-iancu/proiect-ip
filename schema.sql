CREATE TABLE IF NOT EXISTS User (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Temperature (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  value REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS Ingredient (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  measure_unit TEXT NOT NULL,
  available REAL NOT NULL
);

CREATE TABLE IF NOT EXISTS CoffeeRecipe (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  preparation_time REAL
);

CREATE TABLE IF NOT EXISTS CoffeeRecipeIngredient (
  recipe_id INTEGER,
  ingredient_id INTEGER,
  quantity REAL NOT NULL,
  PRIMARY KEY (recipe_id, ingredient_id),
  FOREIGN KEY (ingredient_id) REFERENCES Ingredient (id),
  FOREIGN KEY (recipe_id) REFERENCES CoffeeRecipe (id)
);

CREATE TABLE IF NOT EXISTS CoffeePreparation (
  recipe_id INTEGER,
  started_at TEXT,
  finished_at TEXT,
  ingredients_with_quantities TEXT NOT NULL,
  PRIMARY KEY (recipe_id, started_at),
  FOREIGN KEY (recipe_id) REFERENCES CoffeeRecipe (id)
);

CREATE TABLE IF NOT EXISTS Log (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  type TEXT NOT NULL,
  properties_json TEXT NOT NULL,
  at TEXT NOT NULL
);
