from flask import abort
from http import HTTPStatus
from typing import List
from my_project.auth.service import park_ticket_service
from my_project.auth.domain.orders.park_ticket import ParkTicket
from my_project.auth.controller.general_controller import GeneralController


class ParkTicketController(GeneralController):
    _service = park_ticket_service

    def find_all(self) -> List[ParkTicket]:
        return self._service.get_all()


    def create_park_ticket(self, park_ticket: ParkTicket) -> None:
        self._service.create(park_ticket)


    def find_park_ticket_by_two_id(self, park_id: int, ticket_id: int) -> ParkTicket:
        obj = self._service.get_by_two_id(park_id, ticket_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        return obj


    def update_park_ticket_by_two_id(self, park_id: int, ticket_id: int, in_obj: object) -> ParkTicket:
        obj = self._service.get_by_two_id(park_id, ticket_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        return self._service.update_by_two_id(park_id, ticket_id, in_obj)


    def delete_park_ticket_by_two_id(self, park_id: int, ticket_id: int) -> None:
        obj = self._service.get_by_two_id(park_id, ticket_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(park_id, ticket_id)
