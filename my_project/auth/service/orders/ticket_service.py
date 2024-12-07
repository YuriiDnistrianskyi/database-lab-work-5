from my_project.auth.dao import ticket_dao
from my_project.auth.domain.orders.ticket import Ticket
from my_project.auth.service.general_service import GeneralService


class TicketService(GeneralService):
    _dao = ticket_dao
    _class_type = Ticket
