from flask import Flask

from src.config.Configuration import get_configuration
import src.db as db
import src.controllers.AuthController as auth
import src.controllers.CoffeePreparationController as coffeepreparation
import src.controllers.CoffeeRecipeController as coffeerecipe
import src.controllers.IngredientController as ingredient

app = Flask(__name__)
app.config.from_mapping(SECRET_KEY=get_configuration().auth_secret)

app.register_blueprint(auth.bp)
app.register_blueprint(coffeerecipe.bp)
app.register_blueprint(coffeepreparation.bp)
app.register_blueprint(ingredient.bp)

db.init_app(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>\n"
