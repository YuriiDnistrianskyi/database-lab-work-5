from http import HTTPStatus
from flask import Blueprint, request, Response, make_response, jsonify
from my_project.auth.controller import procedure_price_controller

procedure_price_bp = Blueprint('procedure_sum_price_bp', __name__, url_prefix='/procedure_price')

@procedure_price_bp.get('/<string:ops>')
def function_price(ops: str) -> Response:
    result = procedure_price_controller.activate_procedure_price(ops)
    return make_response(jsonify(result), HTTPStatus.OK)
