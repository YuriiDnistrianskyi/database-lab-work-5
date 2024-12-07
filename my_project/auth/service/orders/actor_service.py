from my_project.auth.dao import actor_dao
from my_project.auth.domain.orders.actor import Actor
from my_project.auth.service.general_service import GeneralService


class ActorService(GeneralService):
    _dao = actor_dao
    _class_type = Actor
