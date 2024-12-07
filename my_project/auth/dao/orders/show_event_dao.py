from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.show_event import ShowEvent


class ShowEventDAO(GeneralDAO):
    _domain_type = ShowEvent
