import datetime
import random
from flask import (
    Blueprint, jsonify, request
)


from src.services.EnvironmentService import EnvironmentService

service = None

bp = Blueprint('environment', __name__, url_prefix='/environment')


def getService():
    global service
    if service is None:
        service = EnvironmentService()
    return service


@bp.route('/temperature', methods=['POST'])
def setTemperature():
    temp = request.json['temp']

    if not temp:
        return jsonify({'status': 'Temp is required.'}), 403

    data = getService().setTemperature(temp)

    return jsonify({
        'status': 'Temperature succesfully recorded',
        'data': {
            'id': data[0],
            'timestamp': data[1],
            'value': data[2]
        }
    }), 201


@bp.route('/temperature', methods=['GET'])
def get_temperature():
    retrieved_temperature = random.randint(-10, 30)

    return jsonify({
        'status': 'Temperature succesfully retrieved',
        'data': {
            'temperature': retrieved_temperature
        }
    }), 200


@bp.route('/currenttime', methods=['GET'])
def get_current_time():
    now = datetime.now()

    current_time = now.strftime("%H:%M")

    return jsonify({
        'status': 'Current time successfully retrieved',
        'data': {
            'current_time': current_time
        }
    }), 200
