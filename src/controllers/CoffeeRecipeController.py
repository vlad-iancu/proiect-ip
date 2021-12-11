from flask import (
    Blueprint, jsonify
)

from src.controllers.AuthController import login_required
from src.services.CoffeeRecipeService import CoffeeRecipeService


class CoffeeRecipeController:
    def __init__(self) -> None:
        self.coffeeRecipeService = CoffeeRecipeService()
        pass

    bp = Blueprint('coffeerecipe', __name__, url_prefix='/coffeerecipes')

    @bp.route('/', methods=['GET'])
    @login_required
    def get_all_coffee_recipes(self):

        data = self.coffeeRecipeService.get_all_coffee_recipes()

        return jsonify({
            'status': 'Coffee recipes successfully retrieved',
            'data': {
                'coffee_recipes': data
            }
        }), 200

    @bp.route('/available', methods=['GET'])
    @login_required
    def get_available_coffees(self):

        data = self.coffeeRecipeService.get_available_coffee_recipes()

        return jsonify({
            'status': 'Available coffees successfully retrieved',
            'data': {
                'available_coffees': data
            }
        }), 200
