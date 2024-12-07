from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import park_show_controller
from my_project.auth.domain.orders.park_show import ParkShow

park_show_bp = Blueprint('ParkShow', __name__, url_prefix='/park_show')

@park_show_bp.get('')
def get_all_park_shows() -> Response:
    park_shows = park_show_controller.find_all()
    park_show_dto = [park_show.put_into_dto() for park_show in park_shows]
    return make_response(jsonify(park_show_dto), HTTPStatus.OK)


@park_show_bp.post('')
def create_park_show() -> Response:
    data = request.get_json()
    park_show = ParkShow.create_from_dto(data)
    park_show_controller.create_park_show(park_show)
    return make_response(jsonify(park_show.put_into_dto()), HTTPStatus.CREATED)


@park_show_bp.get('/<int:park_id>/<int:show_id>')
def get_park_show(park_id: int, show_id: int) -> Response:
    park_show = park_show_controller.find_park_show_by_two_id(park_id, show_id)
    return make_response(jsonify(park_show.put_into_dto()), HTTPStatus.OK)


@park_show_bp.put('/<int:park_id>/<int:show_id>')
def update_park_show(park_id: int, show_id: int) -> Response:
    data = request.get_json()
    park_show = ParkShow.create_from_dto(data)
    park_show_controller.update_park_show(park_id, show_id, park_show)
    return make_response(jsonify({"message": "ParkShow updated"}), HTTPStatus.OK)


@park_show_bp.delete('/<int:park_id>/<int:show_id>')
def delete_park_show(park_id: int, show_id: int) -> Response:
    park_show_controller.delete_park_show(park_id, show_id)
    return make_response(jsonify({"message": "ParkShow deleted"}), HTTPStatus.OK)
