from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import client_controller
from my_project.auth.domain.orders.client import Client

client_bp = Blueprint('client', __name__, url_prefix='/client')

@client_bp.get('')
def get_all_client() -> Response:
    clients = client_controller.find_all()
    client_dto = [client.put_into_dto() for client in clients]
    return make_response(jsonify(client_dto), HTTPStatus.OK)


@client_bp.post('')
def create_client() -> Response:
    data = request.get_json()
    client = Client.create_from_dto(data)
    client_controller.create_client(client)
    return make_response(jsonify(client.put_into_dto()), HTTPStatus.CREATED )


@client_bp.get('/<int:client_id>')
def get_client(client_id: int) -> Response:
    client = client_controller.find_client_by_id(client_id)
    return make_response(jsonify(client.put_into_dto()), HTTPStatus.OK)


@client_bp.put('/<int:clientn_id>')
def update_client(client_id: int) -> Response:
    data = request.get_json()
    client = Client.create_from_dto(data)
    client_controller.update_client(client_id, client)
    return make_response(jsonify({"messange": "Client updated"}), HTTPStatus.OK)


@client_bp.delete('/<int:client_id>')
def delete_client(client_id: int) -> Response:
    client_controller.delete_attraction(client_id)
    return make_response(jsonify({"messange": "Client deleted"}), HTTPStatus.OK)
