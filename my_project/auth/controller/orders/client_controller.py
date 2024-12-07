from flask import abort
from http import HTTPStatus
from typing import List
from my_project.auth.service import client_service
from my_project.auth.domain.orders.client import Client
from my_project.auth.controller.general_controller import GeneralController


class ClientController(GeneralController):
    _service = client_service

    def find_all(self) -> List[Client]:
        return self._service.get_all()


    def create_client(self, client: Client) -> None:
        self._service.create(client)


    def update_client(self, client_id: int, client: Client) -> None:
        obj = self._service.get_by_id(client_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.update(client_id, client)


    def delete_clientr(self, client_id: int) -> None:
        obj = self._service.get_by_id(client_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(client_id)


    def find_client_by_id(self, client_id: int) -> Client:
        obj = self._service.get_by_id(client_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        return obj
