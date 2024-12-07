from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import pass_attraction_controller
from my_project.auth.domain.orders.pass_attraction import PassAttraction

pass_attraction_bp = Blueprint('PassAttraction', __name__, url_prefix='/pass_attraction')

@pass_attraction_bp.get('')
def get_all_pass_attractions() -> Response:
    pass_attractions = pass_attraction_controller.find_all()
    pass_attraction_dto = [pass_attraction.put_into_dto() for pass_attraction in pass_attractions]
    return make_response(jsonify(pass_attraction_dto), HTTPStatus.OK)


@pass_attraction_bp.post('')
def create_pass_attraction() -> Response:
    data = request.get_json()
    pass_attraction = PassAttraction.create_from_dto(data)
    pass_attraction_controller.create_pass_attraction(pass_attraction)
    return make_response(jsonify(pass_attraction.put_into_dto()), HTTPStatus.CREATED)


@pass_attraction_bp.get('/<int:pass_id>/<int:attraction_id>')
def get_pass_attraction(pass_id: int, attraction_id: int) -> Response:
    pass_attraction = pass_attraction_controller.find_pass_attraction_by_two_id(pass_id, attraction_id)
    return make_response(jsonify(pass_attraction.put_into_dto()), HTTPStatus.OK)


@pass_attraction_bp.put('/<int:pass_id>/<int:attraction_id>')
def update_pass_attraction(pass_id: int, attraction_id: int) -> Response:
    data = request.get_json()
    pass_attraction = PassAttraction.create_from_dto(data)
    pass_attraction_controller.update_pass_attraction(pass_id, attraction_id, pass_attraction)
    return make_response(jsonify({"message": "PassAttraction updated"}), HTTPStatus.OK)


@pass_attraction_bp.delete('/<int:pass_id>/<int:attraction_id>')
def delete_pass_attraction(pass_id: int, attraction_id: int) -> Response:
    pass_attraction_controller.delete_pass_attraction(pass_id, attraction_id)
    return make_response(jsonify({"message": "PassAttraction deleted"}), HTTPStatus.OK)
