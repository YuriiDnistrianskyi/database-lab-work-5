from my_project.auth.dao import park_ticket_dao
from my_project.auth.domain.orders.park_ticket import ParkTicket
from my_project.auth.service.general_service import GeneralService


class ParkTicketService(GeneralService):
    _dao = park_ticket_dao
    _class_type = ParkTicket

    def get_by_two_id(self, park_id: int, ticket_id: int) -> _dao:
        return self._dao.get_by_two_id(park_id, ticket_id)


    def update_by_two_id(self, park_id: int, ticket_id: int, obj: _dao):
        self._dao.update_by_two_id(park_id, ticket_id, obj)


    def delete_by_two_id(self, park_id: int, ticket_id: int,):
        self._dao.delete_by_two_id(park_id, ticket_id)
