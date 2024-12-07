from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import park_controller
from my_project.auth.domain.orders.Park import Park

park_bp = Blueprint('park', __name__, url_prefix='/park')

@park_bp.get('')
def get_all_parks() -> Response:
    park = park_controller.find_all()
    park_dto = [park.put_into_dto() for park in park]
    return make_response(jsonify(park_dto), HTTPStatus.OK)


@park_bp.post('')
def create_park() -> Response:
    data = request.get_json()

    park = Park.create_from_dto(data)
    park_controller.create_park(park)
    return make_response(jsonify(park.put_into_dto()), HTTPStatus.CREATED)


@park_bp.post('/params')
def create_by_params() -> Response:
    data = request.get_json()
    park_controller.create_by_params(data)
    return make_response(jsonify({"message": "Created park by parms"}), HTTPStatus.OK)


@park_bp.get('/<int:park_id>')
def get_park(park_id: int) -> Response:
    park = park_controller.find_by_id(park_id)
    if park:
        return make_response(jsonify(park.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Park not found"}), HTTPStatus.NOT_FOUND)


@park_bp.put('/<int:park_id>')
def update_park(park_id: int) -> Response:
    data = request.get_json()
    park = Park.create_from_dto(data)
    park_controller.update_park(park_id, park)
    return make_response(jsonify({"messange": "Park updated"}), HTTPStatus.OK)


@park_bp.delete('/<int:park_id>')
def delete_park(park_id: int) -> Response:
    park_controller.delete_park(park_id)
    return make_response(jsonify({"messange": "Park deleted"}), HTTPStatus.OK)

@park_bp.get('/name/<string:name>')
def get_park_by_name(name: str) -> Response:
    parks = park_controller.find_by_name(name)
    if parks:
        return make_response(jsonify([park.put_into_dto() for park in parks]), HTTPStatus.OK)
    return make_response(jsonify({"error": "Park not found"}), HTTPStatus.NOT_FOUND)

@park_bp.get('/location/<string:location>')
def get_park_by_location(location: str) -> Response:
    parks = park_controller.find_by_location(location)
    if parks:
        return make_response(jsonify([park.put_into_dto() for park in parks]), HTTPStatus.OK)
    return make_response(jsonify({"error": "Park not found"}), HTTPStatus.NOT_FOUND)