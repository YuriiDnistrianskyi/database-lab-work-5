from flask import abort
from http import HTTPStatus
from typing import List
from my_project.auth.service import actor_service
from my_project.auth.domain.orders.actor import Actor
from my_project.auth.controller.general_controller import GeneralController


class ActorController(GeneralController):
    _service = actor_service

    def find_all(self) -> List[Actor]:
        return self._service.get_all()


    def create_actor(self, actor: Actor) -> None:
        self._service.create(actor)


    def update_actor(self, actor_id: int, actor: Actor) -> None:
        obj = self._service.get_by_id(actor_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.update(actor_id, actor)


    def delete_actor(self, actor_id: int) -> None:
        obj = self._service.get_by_id(actor_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(actor_id)


    def find_actor_by_id(self, actor_id: int) -> Actor:
        obj = self._service.get_by_id(actor_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        return obj
