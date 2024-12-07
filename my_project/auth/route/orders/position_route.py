from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import position_controller
from my_project.auth.domain.orders.position import Position

position_bp = Blueprint('position', __name__, url_prefix='/position')

@position_bp.get('')
def get_all_position() -> Response:
    positions = position_controller.find_all()
    if positions:
        employee_dto = [position.put_into_dto() for position in positions]
        return make_response(jsonify(employee_dto), HTTPStatus.OK)
    return make_response(jsonify({"messange": "None"}), HTTPStatus.NOT_FOUND)


@position_bp.post('')
def create_position() -> Response:
    data = request.get_json()
    position = Position.create_from_dto(data)
    position_controller.create_position(position)
    return make_response(jsonify(position.put_into_dto()), HTTPStatus.CREATED )


@position_bp.get('/<int:position_id>')
def get_position(position_id: int) -> Response:
    position = position_controller.find_position_by_id(position_id)
    if position:
        return make_response(jsonify(position.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Position not found"}), HTTPStatus.NOT_FOUND)


@position_bp.put('/<int:position_id>')
def update_position(position_id: int) -> Response:
    data = request.get_json()
    position = Position.create_from_dto(data)
    position_controller.update_position(position_id, position)
    return make_response(jsonify({"messange": "Position updated"}), HTTPStatus.OK)


@position_bp.delete('/<int:position_id>')
def delete_position(position_id: int) -> Response:
    position_controller.delete_position(position_id)
    return make_response(jsonify({"messange": "Position deleted"}), HTTPStatus.OK)