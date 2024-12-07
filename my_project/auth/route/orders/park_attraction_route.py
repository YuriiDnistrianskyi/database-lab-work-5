from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import park_attraction_controller
from my_project.auth.domain.orders.park_attraction import ParkAttraction

park_attraction_bp = Blueprint('park_attraction', __name__, url_prefix='/park_attraction')

@park_attraction_bp.get('')
def get_all_park_attraction() -> Response:
    park_attractions = park_attraction_controller.find_all()
    park_attraction_dto = [park_attraction.put_into_dto() for park_attraction in park_attractions]
    return make_response(jsonify(park_attraction_dto), HTTPStatus.OK)


@park_attraction_bp.post('')
def create_park_attraction() -> Response:
    data = request.get_json()
    park_attraction = ParkAttraction.create_from_dto(data)
    park_attraction_controller.create_park_attraction(park_attraction)
    return make_response(jsonify(park_attraction.put_into_dto()), HTTPStatus.CREATED )


@park_attraction_bp.get('/<int:park_id>/<int:attraction_id>')
def get_park_attraction(park_id: int, attraction_id: int) -> Response:
    park_attraction = park_attraction_controller.find_park_attraction_by_two_id(park_id, attraction_id)
    return make_response(jsonify(park_attraction.put_into_dto()), HTTPStatus.OK)


@park_attraction_bp.put('/<int:park_id>/<int:attraction_id>')
def update_park_attraction(park_id: int, attraction_id) -> Response:
    data = request.get_json()
    park_attraction = ParkAttraction.create_from_dto(data)
    park_attraction_controller.update_park_attraction(park_id, attraction_id, park_attraction)
    return make_response(jsonify({"messange": "ParkAttraction updated"}), HTTPStatus.OK)


@park_attraction_bp.delete('/<int:park_id>/<int:attraction_id>')
def delete_park_attraction(park_id: int, attraction_id) -> Response:
    park_attraction_controller.delete_park_attraction(park_id, attraction_id)
    return make_response(jsonify({"messange": "ParkAttraction deleted"}), HTTPStatus.OK)
