CREATE TABLE `Ingredient` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `measure_unit` varchar(255) NOT NULL,
  `available` float4 NOT NULL
);

CREATE TABLE `CoffeeRecipe` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL
);

CREATE TABLE `CoffeeRecipeIngredient` (
  `recipe_id` int,
  `ingredient_id` int,
  `quantity` float4 NOT NULL,
  PRIMARY KEY (`recipe_id`, `ingredient_id`)
);

CREATE TABLE `CoffeePreparation` (
  `recipe_id` int,
  `started_at` timestamp,
  `finished_at` timestamp,
  `ingredients_json` varchar(255) NOT NULL,
  PRIMARY KEY (`recipe_id`, `started_at`)
);

CREATE TABLE `Log` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `type` varchar(255) NOT NULL,
  `properties_json` varchar(255) NOT NULL,
  `at` timestamp NOT NULL
);

ALTER TABLE `CoffeeRecipeIngredient` ADD FOREIGN KEY (`recipe_id`) REFERENCES `CoffeeRecipe` (`id`);

ALTER TABLE `CoffeeRecipeIngredient` ADD FOREIGN KEY (`ingredient_id`) REFERENCES `Ingredient` (`id`);

ALTER TABLE `CoffeePreparation` ADD FOREIGN KEY (`recipe_id`) REFERENCES `CoffeeRecipe` (`id`);

