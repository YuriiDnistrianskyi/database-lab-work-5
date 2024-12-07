from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.ticket import Ticket


class TicketDAO(GeneralDAO):
    _domain_type = Ticket
