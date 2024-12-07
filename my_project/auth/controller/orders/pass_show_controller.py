from flask import abort
from http import HTTPStatus
from typing import List

from my_project.auth.domain.orders import pass_show
from my_project.auth.service import pass_show_service
from my_project.auth.domain.orders.pass_show import PassShow
from my_project.auth.controller.general_controller import GeneralController


class PassShowController(GeneralController):
    _service = pass_show_service

    def find_all(self) -> List[PassShow]:
        return self._service.get_all()


    def create_pass_show(self, pass_show: PassShow) -> None:
        self._service.create(pass_show)


    def delete_pass_show(self, pass_id: int, show_id: int) -> None:
        obj = self._service.get_by_two_id(pass_id, show_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(pass_id, pass_show)


    def find_pass_show_by_id(self, pass_id: int, show_id: int) -> PassShow:
        obj = self._service.get_by_two_id(pass_id, show_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        return obj
