from flask import (Blueprint, jsonify, request)
from src.controllers.AuthController import login_required
from src.models.Ingredient import Ingredient

from src.services.IngredientService import IngredientService

service = None

bp = Blueprint("ingredient", __name__, url_prefix="/ingredients")


def getService():
    global service
    if service is None:
        service = IngredientService()
    return service


@bp.route("/", methods=["GET"])
def get_all_ingredients():
    data = getService().getAllIngredients()
    return jsonify({
        "status": "All ingredients successfully retrieved",
        "data": {
            "ingredients": list(map(lambda ingredient: ingredient.serialize(), data))
        }
    }), 200


@bp.route("/<id>", methods=["GET"])
def get_ingredient(id):
    ingredient = getService().getIngredientById(id)
    status = ("Ingredient with id " + id + " successfully retrieved.") if ingredient else "Fail"
    code = 200 if ingredient else 400
    return jsonify({
        "status": status,
        "data": {
            "ingredients": ingredient.serialize()
        }
    }), code


@bp.route("/", methods=["POST"])
@login_required
def add_ingredient():
    json_data = request.json
    ingredient: Ingredient = Ingredient(
        0, json_data["name"], json_data["unit"], json_data["available"])
    id = getService().addIngredient(ingredient)
    ingredient.id = id
    return jsonify({
        "status": "Ingredient successfully added",
        "data": {
            "ingredient": ingredient.serialize()
        }
    }), 201


@bp.route("/<id>", methods=["PUT"])
def update_ingredient(id):
    json_data = request.json
    ingredient: Ingredient = Ingredient(
        id, json_data["name"], json_data["unit"], json_data["available"])
    ingredient = getService().updateIngredient(ingredient)
    return jsonify({
        "status": "Ingredient successfully updated",
        "data": {
            "ingredient": ingredient.serialize()
        }
    }), 200


@bp.route("/<id>", methods=["DELETE"])
def delete_ingredient(id):
    deleted = getService().deleteIngredient(id)
    status = "Ingredient successfully deleted" if deleted is not None else "Fail"
    return jsonify({
        "status": status,
        "data": {
            "id": id
        }
    }), 200
