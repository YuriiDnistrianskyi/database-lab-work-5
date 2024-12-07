from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.client import Client


class ClientDAO(GeneralDAO):
    _domain_type = Client
