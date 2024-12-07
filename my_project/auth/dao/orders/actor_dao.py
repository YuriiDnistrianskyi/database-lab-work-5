from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.actor import Actor


class ActorDAO(GeneralDAO):
    _domain_type = Actor
