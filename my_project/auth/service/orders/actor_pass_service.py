from my_project.auth.dao import actor_pass_dao
from my_project.auth.domain.orders.actor_pass import ActorPass
from my_project.auth.service.general_service import GeneralService


class ActorPassService(GeneralService):
    _dao = actor_pass_dao
    _class_type = ActorPass
