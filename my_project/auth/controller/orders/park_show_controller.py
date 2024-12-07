from flask import abort
from http import HTTPStatus
from typing import List
from my_project.auth.service import park_show_service
from my_project.auth.domain.orders.park_show import ParkShow
from my_project.auth.controller.general_controller import GeneralController


class ParkShowController(GeneralController):
    _service = park_show_service

    def find_all(self) -> List[ParkShow]:
        return self._service.get_all()


    def create_park_show(self, park_show: ParkShow) -> None:
        self._service.create(park_show)


    def delete_park_show(self, park_id: int, show_id: int) -> None:
        obj = self._service.get_by_two_id(park_id, show_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(park_id, show_id)


    def find_park_show_by_id(self, park_id: int, show_id: int) -> ParkShow:
        obj = self._service.get_by_two_id(park_id, show_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        return obj
