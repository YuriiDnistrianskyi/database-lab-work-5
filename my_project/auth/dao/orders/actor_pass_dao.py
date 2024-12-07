from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.actor_pass import ActorPass


class ActorPassDAO(GeneralDAO):
    _domain_type = ActorPass
