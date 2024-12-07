from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import ticket_controller
from my_project.auth.domain.orders.ticket import Ticket

ticket_bp = Blueprint('ticket', __name__, url_prefix='/ticket')

@ticket_bp.get('')
def get_all_ticket() -> Response:
    tickets = ticket_controller.find_all()
    ticket_dto = [ticket.put_into_dto() for ticket in tickets]
    return make_response(jsonify(ticket_dto), HTTPStatus.OK)


@ticket_bp.post('')
def create_ticket() -> Response:
    data = request.get_json()
    ticket = Ticket.create_from_dto(data)
    ticket_controller.create_ticket(ticket)
    return make_response(jsonify(ticket.put_into_dto()), HTTPStatus.CREATED )


@ticket_bp.get('/<int:ticket_id>')
def get_ticket(ticket_id: int) -> Response:
    ticket = ticket_controller.find_ticket_by_id(ticket_id)
    return make_response(jsonify(ticket.put_into_dto()), HTTPStatus.OK)


@ticket_bp.put('/<int:ticket_id>')
def update_ticket(ticket_id: int) -> Response:
    data = request.get_json()
    ticket = Ticket.create_from_dto(data)
    ticket_controller.update_ticket(ticket_id, ticket)
    return make_response(jsonify({"messange": "Ticket updated"}), HTTPStatus.OK)


@ticket_bp.delete('/<int:ticket_id>')
def delete_ticket(ticket_id: int) -> Response:
    ticket_controller.delete_ticket(ticket_id)
    return make_response(jsonify({"messange": "Ticket deleted"}), HTTPStatus.OK)
