from flask import (Blueprint, jsonify, request)
from src.models.Ingredient import Ingredient

from src.services.IngredientService import IngredientService

service = None

bp = Blueprint("ingredient", __name__, url_prefix="/ingredient")


def getService():
    global service
    if service is None:
        service = IngredientService()
    return service


@bp.route("/", methods=["GET"])
def get_all_ingredients():
    data = getService().getAllIngredients()
    return jsonify({
        "status": "Success",
        "data": {
            "ingredients": data
        }
    }), 200


@bp.route("/", methods=["POST"])
def add_ingredient():
    json_data = request.json
    ingredient: Ingredient = Ingredient(
        0, json_data["name"], json_data["unit"], json_data["available"])
    id = getService().addIngredient(ingredient)
    ingredient.id = id
    return jsonify({
        "status": "Success",
        "data": {
            "ingredient": ingredient.serialize()
        }
    }), 201


@bp.route("/:id", methods=["PUT"])
def update_ingredient(id):
    json_data = request.json
    ingredient: Ingredient = Ingredient(
        id, json_data["name"], json_data["unit"], json_data["available"])
    ingredient = getService().addIngredient(ingredient)
    return jsonify({
        "status": "Success",
        "data": {
            "ingredient": ingredient.serialize()
        }
    }), 200


@bp.route("/:id", methods=["DELETE"])
def delete_ingredient(id):
    deleted = getService().deleteIngredient(id)
    status = "Success" if deleted else "Fail"
    return jsonify({
        "status": status,
        "data": {
            "id": id
        }
    }), 200
