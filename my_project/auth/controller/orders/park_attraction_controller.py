from flask import abort
from http import HTTPStatus
from typing import List
from my_project.auth.service import park_attraction_service
from my_project.auth.domain.orders.park_attraction import ParkAttraction
from my_project.auth.controller.general_controller import GeneralController


class ParkAttractionController(GeneralController):
    _service = park_attraction_service

    def find_all(self) -> List[ParkAttraction]:
        return self._service.get_all()


    def create_park_attraction(self, park_attraction: ParkAttraction) -> None:
        self._service.create(park_attraction)


    def update_park_attraction(self, park_id: int, attraction_id: int, park_attraction: ParkAttraction) -> None:
        obj = self._service.get_by_two_id(park_id, attraction_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.update_by_two_id(park_id, attraction_id, park_attraction)


    def delete_park_attraction(self, park_id: int, attraction_id: int) -> None:
        obj = self._service.get_by_two_id(park_id, attraction_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete_by_two_id(park_id, attraction_id)


    def find_park_attraction_by_two_id(self, park_id: int, attraction_id: int) -> ParkAttraction:
        obj = self._service.get_by_two_id(park_id, attraction_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        return obj
