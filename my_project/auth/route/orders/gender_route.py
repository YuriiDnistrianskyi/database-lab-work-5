from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import gender_controller
from my_project.auth.domain.orders.gender import Gender

gender_bp = Blueprint('gender', __name__, url_prefix='/gender')

@gender_bp.get('')
def get_all_genders() -> Response:
    genders = gender_controller.find_all()
    if not genders:
        return make_response(jsonify({"messange": "None"}), HTTPStatus.NOT_FOUND)
    gender_dto = [gender.put_into_dto() for gender in genders]
    return make_response(jsonify(gender_dto), HTTPStatus.OK)


@gender_bp.post('')
def create_gender() -> Response:
    data = request.get_json()
    gender = Gender.create_from_dto(data)
    gender_controller.create_gender(gender)
    return make_response(jsonify(gender.put_into_dto()), HTTPStatus.CREATED )


@gender_bp.get('/<int:gender_id>')
def get_gender(gender_id: int) -> Response:
    gender = gender_controller.find_gender_by_id(gender_id)
    if gender:
        return make_response(jsonify(gender.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Gender not found"}), HTTPStatus.NOT_FOUND)


@gender_bp.put('/<int:gender_id>')
def update_gender(gender_id: int) -> Response:
    data = request.get_json()
    gender = Gender.create_from_dto(data)
    gender_controller.update_gender(gender_id, gender)
    return make_response(jsonify({"messange": "Gender updated"}), HTTPStatus.OK)


@gender_bp.delete('/<int:gender_id>')
def delete_gender(gender_id: int) -> Response:
    gender_controller.delete_gender(gender_id)
    return make_response(jsonify({"messange": "Gender deleted"}), HTTPStatus.OK)
