from flask import (
    Blueprint, jsonify, request
)

from src.controllers.AuthController import login_required
from src.services.CoffeePreparationService import CoffeePreparationService


service = None

bp = Blueprint('coffeepreparation', __name__, url_prefix='/coffeepreparations')


def getService():
    global service
    if service is None:
        service = CoffeePreparationService()
    return service

# Prepare coffee endpoint (prepare a recipe with customized ingredients level,
# i.e. send a list of ingredients in the request)


@bp.route('/', methods=['POST'])
@login_required
def prepare_coffee_custom():
    ingredients_names = request.form['ingredients']
    quantities = request.form['quantities']

    if not ingredients_names:
        return jsonify({'status': 'Ingredients are required.'}), 403

    if not quantities:
        return jsonify({'status': 'Quantities for ingredients are required.'}), 403

    if len(quantities) != len(ingredients_names):
        return jsonify({'status': 'Quantities are required for each ingredient.'}), 403

    data = getService().prepare_coffee_custom(ingredients_names, quantities)

    return jsonify({
        'status': 'Coffee successfully prepared',
        'data': {
            'ingredients available': data
        }
    }), 200

# Prepare coffee endpoint (prepare a premade recipe,  i.e. send recipe
# name in the request)


@bp.route('/', methods=['POST'])
@login_required
def prepare_coffee_premade():
    recipe_name = request.form['recipe']

    if not recipe_name:
        return jsonify({'status': 'Recipe name is required.'}), 403

    print('Recipe name: ' + recipe_name)

    data = getService().prepare_coffee_premade(recipe_name)

    if data is None:
        return jsonify({'status': 'There is no recipe with the given recipe name.'}), 403

    return jsonify({
        'status': 'Coffee successfully prepared',
        'data': {
            'ingredients available': data
        }
    }), 200


@bp.route('/', methods=['GET'])
@login_required
def get_all_prepared_coffees():

    data = getService().get_all_coffee_preparations()

    return jsonify({
        'status': 'Coffee preparations successfully retrieved',
        'data': {
            'coffee_preparations': data
        }
    }), 200


@bp.route('/last', methods=['GET'])
@login_required
def get_last_prepared_coffee():

    data = getService().get_last_coffee_preparation()

    return jsonify({
        'status': 'Last coffee prepared successfully retrieved',
        'data': {
            'last_coffee_prepared': data
        }
    }), 200
