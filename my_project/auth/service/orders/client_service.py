from my_project.auth.dao import client_dao
from my_project.auth.domain.orders.client import Client
from my_project.auth.service.general_service import GeneralService


class ClientService(GeneralService):
    _dao = client_dao
    _class_type = Client
