from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import park_employee_controller
from my_project.auth.domain.orders.park_employee import ParkEmployee

park_employee_bp = Blueprint('ParkEmployee', __name__, url_prefix='/park_employee')

@park_employee_bp.get('')
def get_all_park_employee() -> Response:
    park_employees = park_employee_controller.find_all()
    if park_employees:
        park_employee_dto = [park_employee.put_into_dto() for park_employee in park_employees]
        return make_response(jsonify(park_employee_dto), HTTPStatus.OK)
    return make_response(jsonify({"messange": "None"}), HTTPStatus.NOT_FOUND)


@park_employee_bp.post('')
def create_park_employee() -> Response:
    data = request.get_json()
    park_employee = ParkEmployee.create_from_dto(data)
    park_employee_controller.create_park_employee(park_employee)
    return make_response(jsonify(park_employee.put_into_dto()), HTTPStatus.CREATED )



@park_employee_bp.get('/<int:park_id>/<int:employee_id>')
def get_park_employee(park_id: int, employee_id: int) -> Response:
    park_attraction = park_employee_controller.find_park_employee_by_two_id(park_id, employee_id)
    return make_response(jsonify(park_attraction.put_into_dto()), HTTPStatus.OK)


@park_employee_bp.put('/<int:park_id>/<int:employee_id>')
def update_park_employee(park_id: int, employee_id: int) -> Response:
    data = request.get_json()
    park_employee = ParkEmployee.create_from_dto(data)
    park_employee_controller.update_park_employee(park_id, employee_id, park_employee)
    return make_response(jsonify(park_employee.put_into_dto()), HTTPStatus.OK)


@park_employee_bp.delete('/<int:park_id>/<int:employee_id>')
def delete_park_employee(park_id: int, employee_id) -> Response:
    park_employee_controller.delete_park_employee(park_id, employee_id)
    return make_response(jsonify({"messange": "ParkAttraction deleted"}), HTTPStatus.OK)
