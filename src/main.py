from flask import Flask

import src.db as db
import src.controllers.AuthController as auth
from src.controllers.CoffeePreparationController import CoffeePreparationController as coffeepreparation
from src.controllers.CoffeeRecipeController import CoffeeRecipeController as coffeerecipe

app = Flask(__name__)

app.register_blueprint(auth.bp)
app.register_blueprint(coffeerecipe.bp)
app.register_blueprint(coffeepreparation.bp)

db.init_app(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>\n"
