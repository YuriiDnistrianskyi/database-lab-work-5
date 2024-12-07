from flask import abort
from http import HTTPStatus
from typing import List
from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.domain.orders.park_employee import ParkEmployee
from my_project.auth.service import park_employee_service


class ParkEmployeeController(GeneralController):
    _service = park_employee_service

    def find_all(self) -> List[ParkEmployee]:
        return self._service.get_all()


    def create_park_employee(self, park_employee: ParkEmployee) -> None:
        self._service.create(park_employee)  #


    def update_park_employee(self, park_id: int, employee_id: int, park_employee: ParkEmployee) -> None:
        obj = self._service.get_by_two_id(park_id, employee_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.update_by_two_id(park_id, employee_id, park_employee)


    def delete_park_employee(self, park_id: int, employee_id: int) -> None:
        obj = self._service.get_by_two_id(park_id, employee_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete_by_two_id(park_id, employee_id)


    def find_park_employee_by_two_id(self, park_id: int, employee_id: int) -> ParkEmployee:
        obj = self._service.get_by_two_id(park_id, employee_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        return obj
