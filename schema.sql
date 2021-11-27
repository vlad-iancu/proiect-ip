CREATE TABLE Ingredient (
  id integer PRIMARY KEY AUTOINCREMENT,
  name varchar(255) NOT NULL,
  measure_unit varchar(255) NOT NULL,
  available DECIMAL(10,5) NOT NULL
);

CREATE TABLE CoffeeRecipe (
  id integer PRIMARY KEY AUTOINCREMENT,
  name varchar(255) NOT NULL
);

CREATE TABLE CoffeeRecipeIngredient (
  recipe_id int,
  ingredient_id int,
  quantity DECIMAL(10,5) NOT NULL,
  PRIMARY KEY (recipe_id, ingredient_id),
  FOREIGN KEY (recipe_id) REFERENCES CoffeeRecipe (id),
  FOREIGN KEY (ingredient_id) REFERENCES Ingredient (id)
);

CREATE TABLE CoffeePreparation (
  recipe_id int,
  started_at timestamp,
  finished_at timestamp,
  ingredients_json varchar(255) NOT NULL,
  PRIMARY KEY (recipe_id, started_at),
  FOREIGN KEY (recipe_id) REFERENCES CoffeeRecipe (id)
);

CREATE TABLE Log (
  id integer PRIMARY KEY AUTOINCREMENT,
  type varchar(255) NOT NULL,
  properties_json varchar(255) NOT NULL,
  at timestamp NOT NULL
);