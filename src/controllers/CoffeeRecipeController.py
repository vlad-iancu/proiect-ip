import ast
from flask import (
    Blueprint, jsonify, request
)

from src.controllers.AuthController import login_required
from src.models.CoffeeRecipe import CoffeeRecipe
from src.services.CoffeeRecipeService import CoffeeRecipeService

service = None

bp = Blueprint('coffeerecipe', __name__, url_prefix='/coffeerecipes')


def getService():
    global service
    if service is None:
        service = CoffeeRecipeService()
    return service


@bp.route('/', methods=['GET'])
def getAll():

    data = getService().getAll()

    return jsonify({
        'status': 'Coffee recipes successfully retrieved',
        'data': {
            'coffee_recipes': list(map(lambda coffeerecipe: coffeerecipe.serialize(), data))
        }
    }), 200


@bp.route('/recommendations', methods=['GET'])
def getRecommendedCoffeeRecipes():
    """
    Returns recommended coffee recipe(s) based on time and temperature (max. 2 recommendations)

    :param current_time: Current time in str. format 'HH:MM'
    :param temperature: Integer temperature in str. format
    :return: List of strings (CoffeeRecipe names)
    """
    current_time = request.form['current_time']
    temperature = request.form['temperature']

    data = getService().getRecommendations(current_time, temperature)

    return jsonify({
        'status': 'Coffee recommendations successfully retrieved',
        'data': {
            'recommendations': data
        }
    }), 200


@bp.route('/', methods=['POST'])
@login_required
def add():
    coffee_recipe = request.form['coffee_recipe']

    if not coffee_recipe['name']:
        return jsonify({'status': 'Coffee recipe name is required.'}), 400

    if not coffee_recipe['preparation_time']:
        return jsonify({'status': 'Coffee preparation time is required.'}), 400

    if not coffee_recipe['ingredients_with_quantity']:
        return jsonify({'status': 'Coffee recipe ingredients (min. 1) are required.'}), 400

    recipe: CoffeeRecipe = CoffeeRecipe()
    recipe.name = coffee_recipe['name']
    recipe.preparation_time = float(coffee_recipe['preparation_time'])
    recipe.ingredients_with_quantities = list(
        ast.literal_eval(coffee_recipe['ingredients_with_quantity']))

    data = getService().add(coffee_recipe)

    return jsonify({
        'status': 'Coffee recipe succesfully added',
        'data': {
            'added_recipe': data.serialize()
        }
    }), 201


@bp.route('/available', methods=['GET'])
def getAvailableCoffeeRecipes():

    data = getService().getAvailable()

    return jsonify({
        'status': 'Available coffee recipes successfully retrieved',
        'data': {
            'available_coffees': list(map(lambda coffeerecipe: coffeerecipe.serialize(), data))
        }
    }), 200
