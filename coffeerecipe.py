from flask import (
    Blueprint, request, jsonify
)

from auth import login_required
from db import get_db

bp = Blueprint('coffeerecipe', __name__, url_prefix='/coffeerecipe')

@bp.route('/all', methods=['GET'])
@login_required
def get_all_coffee_recipes():
    coffee_recipes = get_db().execute('SELECT * FROM coffeerecipe').fetchall()
    data = []
    for coffee_recipe in coffee_recipes:
        data.append([x for x in coffee_recipe])

    return jsonify({
        'status': 'Coffee recipes successfully retrieved',
        'data': {
            'coffee_recipes': data
        }
    }), 200

@bp.route('/availables', methods=['GET'])
@login_required
def get_available_coffees():
    available_coffees = get_db().execute(
        'SELECT cri1.name FROM coffeerecipe cri1, ' +
        '(SELECT recipe_id, count(*) as no_ingredients_total ' +
        'FROM coffeerecipeingredient cri JOIN ingredient i ' +
        'WHERE cri.ingredient_id = i.id GROUP BY cri.recipe_id) cri2,' +
        '(SELECT recipe_id, count(*) as no_ingredients_available ' +
        'FROM coffeerecipeingredient JOIN ingredient i ' +
        'WHERE ingredient_id = id AND quantity <= available ' +
        'GROUP BY recipe_id) cri3 ' + 
        'WHERE cri1.id = cri2.recipe_id ' +
        'AND cri2.recipe_id = cri3.recipe_id ' +
        'AND cri2.no_ingredients_total = cri3.no_ingredients_available').fetchall()

    data = []
    for available_coffee in available_coffees:
        data.append([x for x in available_coffee]) # or simply data.append(list(row))

    return jsonify({
        'status': 'Available coffees successfully retrieved',
        'data': {
            'available_coffees': data
        }
    }), 200
