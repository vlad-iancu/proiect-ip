INSERT INTO Ingredient (name, measure_unit, available) VALUES (water, ml, 500);
INSERT INTO Ingredient (name, measure_unit, available) VALUES (milk, ml, 300);
INSERT INTO Ingredient (name, measure_unit, available) VALUES (sugar, gr, 350);
INSERT INTO Ingredient (name, measure_unit, available) VALUES (cocoa, gr, 200);
INSERT INTO Ingredient (name, measure_unit, available) VALUES (whipped cream, ml, 100);
INSERT INTO Ingredient (name, measure_unit, available) VALUES (syrup, ml, 50);
INSERT INTO Ingredient (name, measure_unit, available) VALUES (whiskey, ml, 30);
INSERT INTO Ingredient (name, measure_unit, available) VALUES (coffee, gr, 400);

INSERT INTO CoffeeRecipe (name) VALUES (Irish Coffee);
INSERT INTO CoffeeRecipe (name) VALUES (Hot Chocolate);
INSERT INTO CoffeeRecipe (name) VALUES (Short Espresso);
INSERT INTO CoffeeRecipe (name) VALUES (Long Espresso);
INSERT INTO CoffeeRecipe (name) VALUES (Cappuccino);
INSERT INTO CoffeeRecipe (name) VALUES (Caramel Frappe);
INSERT INTO CoffeeRecipe (name) VALUES (Mocha);

INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (1, 5, 50);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (1, 7, 10);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (1, 8, 50);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (2, 4, 100);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (2, 1, 250);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (2, 3, 50);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (3, 8, 150);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (3, 1, 50);
INSERT INTO CoffeeRecipeIngredient` (recipe_id, ingredient_id, quantity) VALUES (4, 8, 50);
INSERT INTO CoffeeRecipeIngredient` (recipe_id, ingredient_id, quantity) VALUES (4, 1, 150);
INSERT INTO CoffeeRecipeIngredient` (recipe_id, ingredient_id, quantity) VALUES (5, 8, 100);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (5, 2, 200);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (6, 6, 30);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (6, 3, 50);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (6, 5, 50);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (6, 2, 300);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (6, 8, 50);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (7, 8, 50);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (7, 2, 200);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (7, 5, 50);
INSERT INTO CoffeeRecipeIngredient (recipe_id, ingredient_id, quantity) VALUES (7, 4, 80);
