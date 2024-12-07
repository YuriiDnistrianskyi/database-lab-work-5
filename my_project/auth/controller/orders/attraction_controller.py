from flask import abort
from typing import List
from http import HTTPStatus
from my_project.auth.service import attraction_service
from my_project.auth.domain.orders.attraction import Attraction
from my_project.auth.controller.general_controller import GeneralController

class AttractionController(GeneralController):
    _service = attraction_service


    def create_attraction(self, attraction: Attraction) -> None:
        self._service.create(attraction)

    def update_attraction(self, attraction_id: int, attraction: Attraction) -> None:
        obj = self._service.get_by_id(attraction_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.update(attraction_id, attraction)

    def delete_attraction(self, attraction_id: int) -> None:
        obj = self._service.get_by_id(attraction_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(attraction_id)

    def find_all(self) -> List[Attraction]:
        return self._service.get_all()

    def find_attraction_by_id(self, attraction_id: int) -> Attraction:
        obj = self._service.get_by_id(attraction_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        return self._service.get_by_id(attraction_id)

    def find_attraction_by_name(self, name: str) -> List[Attraction]:
        return self._service.get_by_name(name)

    def find_attraction_by_capacity(self, capacity: str) -> List[Attraction]:
        return self._service.get_by_capacity(capacity)
