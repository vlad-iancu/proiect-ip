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


@bp.route('/custom', methods=['POST'])
@login_required
def prepareCoffeeCustom():
    """
    Prepares a coffee recipe with customized ingredients level
    :ingredient_names: Request param. that is a list of the ingredient names for the recipe
    :ingredient_quantities: Request param. that is a list of the quantities for each ingredient for the recipe
    """
    recipe_id = request.json['recipe_id']
    ingredient_names = request.json['ingredient_names']
    ingredient_quantities = request.json['ingredient_quantities']

    if not recipe_id:
        return jsonify({'status': 'Recipe id is required.'}), 400

    if not ingredient_names:
        return jsonify({'status': 'Ingredients are required.'}), 400

    if not ingredient_quantities:
        return jsonify({'status': 'Quantities for ingredients are required.'}), 400

    data = getService().prepareCoffeeCustom(recipe_id, ingredient_names, ingredient_quantities)

    if data is None:
        return jsonify({'status': 'Coffee could not be prepared.'}), 500

    return jsonify({
        'status': 'Coffee successfully prepared',
        'data': {
            'prepared_coffee': data.serialize()
        }
    }), 201


@bp.route('/', methods=['POST'])
@login_required
def prepareCoffeePremade():
    """
    Prepares a premade coffee recipe
    :recipe_name: Request param. to indicate  of the recipe to prepare
    """
    recipe_name = request.json['recipe_name']

    if not recipe_name:
        return jsonify({'status': 'Recipe name is required.'}), 400

    print('Recipe name: ' + recipe_name)

    data = getService().prepareCoffeePremade(recipe_name)

    if data is None:
        return jsonify({'status': 'There is no coffee recipe with the given name.'}), 404

    return jsonify({
        'status': 'Coffee successfully prepared',
        'data': {
            'prepared_coffee': data.serialize()
        }
    }), 201


@bp.route('/', methods=['GET'])
def getAllPreparedCoffees():

    data = getService().getAll()

    return jsonify({
        'status': 'All coffee preparations successfully retrieved',
        'data': {
            'all_prepared_coffees': list(map(lambda coffeepreparation: coffeepreparation.serialize(), data))
        }
    }), 200


@bp.route('/last', methods=['GET'])
def getLastPreparedCoffee():

    data = getService().getLastPrepared()

    if data is None:
        return jsonify({
            'status': 'Last prepared coffee successfully retrieved',
            'data': {
                'last_prepared_coffee': 'No coffee has been prepared yet'
            }
        }), 200

    return jsonify({
        'status': 'Last prepared coffee successfully retrieved',
        'data': {
            'last_prepared_coffee': data.serialize()
        }
    }), 200
