from flask import (
    Blueprint, jsonify
)

from src.controllers.AuthController import login_required
from src.services.CoffeePreparationService import CoffeePreparationService


class CoffeePreparationController:

    def __init__(self) -> None:
        self.coffeePreparationService = CoffeePreparationService()
        pass

    bp = Blueprint('coffeepreparation', __name__, url_prefix='/coffeepreparations')

    @bp.route('/', methods=['GET'])
    @login_required
    def get_all_prepared_coffees(self):

        data = self.coffeePreparationService.get_all_coffee_preparations()

        return jsonify({
            'status': 'Coffee preparations successfully retrieved',
            'data': {
                'coffee_preparations': data
            }
        }), 200

    @bp.route('/last', methods=['GET'])
    @login_required
    def get_last_prepared_coffee(self):

        data = self.coffeePreparationService.get_last_coffee_preparation()

        return jsonify({
            'status': 'Last coffee prepared successfully retrieved',
            'data': {
                'last_coffee_prepared': data
            }
        }), 200
