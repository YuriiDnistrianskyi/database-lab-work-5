from my_project.auth.dao import position_dao
from my_project.auth.domain.orders.position import Position
from my_project.auth.service.general_service import GeneralService


class PositionService(GeneralService):
    _dao = position_dao
    _class_type = Position
