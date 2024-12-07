from http import HTTPStatus
from flask import Blueprint, Response, make_response, jsonify
from my_project.auth.controller import create_random_tables_controller

create_random_tables_bp = Blueprint('create_random_tables', __name__, url_prefix='/create_random_tables')

@create_random_tables_bp.get('')
def insert_in_position() -> Response:
    create_random_tables_controller.activate_procedure_create_random_tables()
    return make_response(jsonify({'message': 'Created tables (FROM Park)'}), HTTPStatus.OK)