from flask import abort
from http import HTTPStatus
from typing import List

from my_project.auth.domain.orders import pass_attraction
from my_project.auth.service import pass_attraction_service
from my_project.auth.domain.orders.pass_attraction import PassAttraction
from my_project.auth.controller.general_controller import GeneralController


class PassAttractionController(GeneralController):
    _service = pass_attraction_service

    def find_all(self) -> List[PassAttraction]:
        return self._service.get_all()


    def create_pass_attraction(self, pass_attraction: PassAttraction) -> None:
        self._service.create(pass_attraction)



    def delete_pass_attraction(self, pass_id: int, attraction_id: int) -> None:
        obj = self._service.get_by_two_id(pass_id, attraction_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(pass_id, pass_attraction)


    def find_pass_attraction_by_id(self, pass_id: int, attraction_id: int) -> PassAttraction:
        obj = self._service.get_by_two_id(pass_id, attraction_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        return obj
