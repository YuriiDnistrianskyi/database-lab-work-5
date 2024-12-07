from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.position import Position


class PositionDAO(GeneralDAO):
    _domain_type = Position
