from os import abort
from http import HTTPStatus
from typing import List
from my_project.auth.service import position_service
from my_project.auth.domain.orders.position import Position
from my_project.auth.controller.general_controller import GeneralController

class PositionController(GeneralController):
    _service = position_service

    def create_position(self, position: Position) -> None:
        self._service.create(position)

    def update_position(self, position_id: int, park: Position) -> None:
        position = self._service.get_by_id(position_id)
        if not position:
            abort(HTTPStatus.NOT_FOUNT)
        self._service.update(position_id, park)

    def delete_position(self, position_id: int) -> None:
        position = self._service.get_by_id(position_id)
        if not position:
            abort(HTTPStatus.NOT_FOUNT)
        self._service.delete(position_id)

    def find_all(self) -> List[Position]:
        return self._service.get_all()

    def find_position_by_id(self, position_id: int) -> Position:
        return self._service.get_by_id(position_id)
