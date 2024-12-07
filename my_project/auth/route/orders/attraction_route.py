from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import attraction_controller
from my_project.auth.domain.orders.attraction import Attraction

attraction_bp = Blueprint('attraction', __name__, url_prefix='/attraction')

@attraction_bp.get('')
def get_all_attractions() -> Response:
    attractions = attraction_controller.find_all()
    attraction_dto = [attraction.put_into_dto() for attraction in attractions]
    return make_response(jsonify(attraction_dto), HTTPStatus.OK)


@attraction_bp.post('')
def create_attraction() -> Response:
    data = request.get_json()
    attraction = Attraction.create_from_dto(data)
    attraction_controller.create_attraction(attraction)
    return make_response(jsonify(attraction.put_into_dto()), HTTPStatus.CREATED )


@attraction_bp.get('/<int:attraction_id>')
def get_attraction(attraction_id: int) -> Response:
    attraction = attraction_controller.find_attraction_by_id(attraction_id)
    return make_response(jsonify(attraction.put_into_dto()), HTTPStatus.OK)


@attraction_bp.put('/<int:attraction_id>')
def update_attraction(attraction_id: int) -> Response:
    data = request.get_json()
    attraction = Attraction.create_from_dto(data)
    attraction_controller.update_attraction(attraction_id, attraction)
    return make_response(jsonify({"messange": "Attraction updated"}), HTTPStatus.OK)


@attraction_bp.delete('/<int:attraction_id>')
def delete_attraction(attraction_id: int) -> Response:
    attraction_controller.delete_attraction(attraction_id)
    return make_response(jsonify({"messange": "Attraction deleted"}), HTTPStatus.OK)


@attraction_bp.get('/name/<string:name>')
def get_attraction_by_name(name: str) -> Response:
    attractions = attraction_controller.find_attraction_by_name(name)
    if attractions:
        return make_response(jsonify([attraction.put_into_dto() for attraction in attractions]), HTTPStatus.OK)
    return make_response(jsonify({"error": "Attractions not found"}), HTTPStatus.NOT_FOUND)


@attraction_bp.get('/capacity/<int:capacity>')
def get_attraction_by_capacity(capacity: int) -> Response:
    attractions = attraction_controller.find_attraction_by_capacity(capacity)
    if attractions:
        return make_response(jsonify([attraction.put_into_dto() for attraction in attractions]), HTTPStatus.OK)
    return make_response(jsonify({"error": "Attractions not found"}), HTTPStatus.NOT_FOUND)
