from flask import abort
from http import HTTPStatus
from typing import List
from my_project.auth.service import ticket_service
from my_project.auth.domain.orders.ticket import Ticket
from my_project.auth.controller.general_controller import GeneralController


class TicketController(GeneralController):
    _service = ticket_service

    def find_all(self) -> List[Ticket]:
        return self._service.get_all()


    def create_ticket(self, ticket: Ticket) -> None:
        self._service.create(ticket)


    def update_ticket(self, ticket_id: int, ticket: Ticket) -> None:
        obj = self._service.get_by_id(ticket_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.update(ticket_id, ticket)


    def delete_ticket(self, ticket_id: int) -> None:
        obj = self._service.get_by_id(ticket_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(ticket_id)


    def find_ticket_by_id(self, ticket_id: int) -> Ticket:
        obj = self._service.get_by_id(ticket_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        return obj
