from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import park_ticket_controller
from my_project.auth.domain.orders.park_ticket import ParkTicket

park_ticket_bp = Blueprint('ParkTicket', __name__, url_prefix='/park_ticket')

@park_ticket_bp.get('')
def get_all_park_tickets() -> Response:
    park_tickets = park_ticket_controller.find_all()
    park_ticket_dto = [park_ticket.put_into_dto() for park_ticket in park_tickets]
    return make_response(jsonify(park_ticket_dto), HTTPStatus.OK)


@park_ticket_bp.post('')
def create_park_ticket() -> Response:
    data = request.get_json()
    park_ticket = ParkTicket.create_from_dto(data)
    park_ticket_controller.create_park_ticket(park_ticket)
    return make_response(jsonify(park_ticket.put_into_dto()), HTTPStatus.CREATED)


@park_ticket_bp.get('/<int:park_id>/<int:ticket_id>')
def get_park_ticket(park_id: int, ticket_id: int) -> Response:
    park_ticket = park_ticket_controller.find_park_ticket_by_two_id(park_id, ticket_id)
    return make_response(jsonify(park_ticket.put_into_dto()), HTTPStatus.OK)


@park_ticket_bp.put('/<int:park_id>/<int:ticket_id>')
def update_park_ticket(park_id: int, ticket_id: int) -> Response:
    data = request.get_json()
    park_ticket = ParkTicket.create_from_dto(data)
    park_ticket_controller.update_park_ticket_by_two_id(park_id, ticket_id, park_ticket)
    return make_response(jsonify({"message": "ParkTicket updated"}), HTTPStatus.OK)


@park_ticket_bp.delete('/<int:park_id>/<int:ticket_id>')
def delete_park_ticket(park_id: int, ticket_id: int) -> Response:
    park_ticket_controller.delete_park_ticket(park_id, ticket_id)
    return make_response(jsonify({"message": "ParkTicket deleted"}), HTTPStatus.OK)
