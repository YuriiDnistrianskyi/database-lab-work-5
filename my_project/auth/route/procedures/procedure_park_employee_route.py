from http import HTTPStatus
from flask import Blueprint, request, Response, make_response, jsonify
from my_project.auth.controller import procedure_park_employee_controller

procedure_park_employee_bp = Blueprint('procedure_park_employee', __name__, url_prefix='/procedure_park_employee')

@procedure_park_employee_bp.get('')
def function_price() -> Response:
    data = request.get_json()
    park_id = data['park_id']
    employee_id = data['employee_id']
    procedure_park_employee_controller.activate_procedure_park_employee(park_id, employee_id)
    return make_response(jsonify({"message": "Create ParkEmployee"}), HTTPStatus.OK)
