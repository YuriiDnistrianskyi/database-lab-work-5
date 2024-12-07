from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import pass_show_controller
from my_project.auth.domain.orders.pass_show import PassShow

pass_show_bp = Blueprint('PassShow', __name__, url_prefix='/pass_show')

@pass_show_bp.get('')
def get_all_pass_shows() -> Response:
    pass_shows = pass_show_controller.find_all()
    pass_show_dto = [pass_show.put_into_dto() for pass_show in pass_shows]
    return make_response(jsonify(pass_show_dto), HTTPStatus.OK)


@pass_show_bp.post('')
def create_pass_show() -> Response:
    data = request.get_json()
    pass_show = PassShow.create_from_dto(data)
    pass_show_controller.create_pass_show(pass_show)
    return make_response(jsonify(pass_show.put_into_dto()), HTTPStatus.CREATED)


@pass_show_bp.get('/<int:pass_id>/<int:show_id>')
def get_pass_show(pass_id: int, show_id: int) -> Response:
    pass_show = pass_show_controller.find_pass_show_by_two_id(pass_id, show_id)
    return make_response(jsonify(pass_show.put_into_dto()), HTTPStatus.OK)


@pass_show_bp.put('/<int:pass_id>/<int:show_id>')
def update_pass_show(pass_id: int, show_id: int) -> Response:
    data = request.get_json()
    pass_show = PassShow.create_from_dto(data)
    pass_show_controller.update_pass_show(pass_id, show_id, pass_show)
    return make_response(jsonify({"message": "PassShow updated"}), HTTPStatus.OK)


@pass_show_bp.delete('/<int:pass_id>/<int:show_id>')
def delete_pass_show(pass_id: int, show_id: int) -> Response:
    pass_show_controller.delete_pass_show(pass_id, show_id)
    return make_response(jsonify({"message": "PassShow deleted"}), HTTPStatus.OK)
