from my_project.auth.dao import show_event_dao
from my_project.auth.domain.orders.show_event import ShowEvent
from my_project.auth.service.general_service import GeneralService


class ShowEventService(GeneralService):
    _dao = show_event_dao
    _class_type = ShowEvent
