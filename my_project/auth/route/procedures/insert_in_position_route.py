from http import HTTPStatus
from flask import Blueprint, Response, make_response, jsonify
from my_project.auth.controller import insert_in_position_controller

insert_in_position_bp = Blueprint('insert_in_position', __name__, url_prefix='/insert_in_position')

@insert_in_position_bp.get('')
def insert_in_position() -> Response:
    insert_in_position_controller.activate_procedure_insert_in_position()
    return make_response(jsonify({'message': 'insert 10 rows in Position'}), HTTPStatus.OK)