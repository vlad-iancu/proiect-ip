from flask import Flask

import src.db as db
import src.controllers.AuthController as auth
import src.controllers.CoffeePreparationController as coffeepreparation
import src.controllers.CoffeeRecipeController as coffeerecipe

app = Flask(__name__)

app.register_blueprint(auth.bp)
app.register_blueprint(coffeerecipe.bp)
app.register_blueprint(coffeepreparation.bp)

db.init_app(app)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
