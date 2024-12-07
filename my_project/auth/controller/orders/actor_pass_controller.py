from flask import abort
from typing import List
from http import HTTPStatus
from my_project.auth.service import actor_pass_service
from my_project.auth.domain.orders.actor_pass import ActorPass
from my_project.auth.controller.general_controller import GeneralController


class ActorPassController(GeneralController):
    _service = actor_pass_service

    def find_all(self) -> List[ActorPass]:
        return self._service.get_all()


    def create_actor_pass(self, actor_pass: ActorPass) -> None:
        self._service.create(actor_pass)


    def update_actor_pass(self, actor_pass_id: int, actor_pass: ActorPass) -> None:
        obj = self._service.get_by_id(actor_pass_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.update(actor_pass_id, actor_pass)


    def delete_actor_pass(self, actor_pass_id: int) -> None:
        obj = self._service.get_by_id(actor_pass_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(actor_pass_id)


    def find_actor_pass_by_id(self, attraction_id: int) -> ActorPass:
        obj = self._service.get_by_id(attraction_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        return obj
