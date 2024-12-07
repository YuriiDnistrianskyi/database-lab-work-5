from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import employee_controller
from my_project.auth.domain.orders.employee import Employee

employee_bp = Blueprint('Employee', __name__, url_prefix='/employee')

@employee_bp.get('')
def get_all_employees() -> Response:
    employees = employee_controller.find_all()
    if employees:
        employee_dto = [employee.put_into_dto() for employee in employees]
        return make_response(jsonify(employee_dto), HTTPStatus.OK)
    return make_response(jsonify({"messange": "None"}), HTTPStatus.NOT_FOUND)


@employee_bp.post('')
def create_employee() -> Response:
    data = request.get_json()
    employee = Employee.create_from_dto(data)
    employee_controller.create_employee(employee)
    return make_response(jsonify(employee.put_into_dto()), HTTPStatus.CREATED )


@employee_bp.get('/<int:employee_id>')
def get_employee(employee_id: int) -> Response:
    employee = employee_controller.find_employee_by_id(employee_id)
    if employee:
        return make_response(jsonify(employee.put_into_dto()), HTTPStatus.OK)
    return make_response(jsonify({"error": "Employee not found"}), HTTPStatus.NOT_FOUND)


@employee_bp.put('/<int:employee_id>')
def update_attraction(employee_id: int) -> Response:
    data = request.get_json()
    employee = Employee.create_from_dto(data)
    employee_controller.update_employee(employee_id, employee)
    return make_response(jsonify({"messange": "Employee updated"}), HTTPStatus.OK)


@employee_bp.delete('/<int:employee_id>')
def delete_employee(employee_id: int) -> Response:
    employee_controller.delete_employee(employee_id)
    return make_response(jsonify({"messange": "Employee deleted"}), HTTPStatus.OK)


@employee_bp.get('/first_name/<string:first_name>')
def get_employee_by_name(first_name: str) -> Response:
    employees = employee_controller.find_employee_by_first_name(first_name)
    if employees:
        return make_response(jsonify([employee.put_into_dto() for employee in employees]), HTTPStatus.OK)
    return make_response(jsonify({"error": "Employees not found"}), HTTPStatus.NOT_FOUND)

"""
@employee_bp.get('/last_name/<string:last_name>')
def get_employee_by_name(last_name: str) -> Response:
    employees = employee_controller.find_employee_by_last_name(last_name)
    if employees:
        return make_response(jsonify([employee.put_into_dto() for employee in employees]), HTTPStatus.OK)
    return make_response(jsonify({"error": "Employees not found"}), HTTPStatus.NOT_FOUND)
"""


