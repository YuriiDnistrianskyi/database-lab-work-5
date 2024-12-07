from flask import abort
from http import HTTPStatus
from typing import List
from my_project.auth.service import employee_pass_service
from my_project.auth.domain.orders.employee_pass import EmployeePass
from my_project.auth.controller.general_controller import GeneralController


class EmployeePassController(GeneralController):
    _service = employee_pass_service

    def find_all(self) -> List[EmployeePass]:
        return self._service.get_all()


    def create_employee_pass(self, employee_pass: EmployeePass) -> None:
        self._service.create(employee_pass)


    def update_employee_pass(self, employee_pass_id: int, employee_pass: EmployeePass) -> None:
        obj = self._service.get_by_id(employee_pass_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.update(employee_pass_id, employee_pass)


    def delete_employee_pass(self, employee_pass_id: int) -> None:
        obj = self._service.get_by_id(employee_pass_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(employee_pass_id)


    def find_employee_pass_by_id(self, employee_pass_id: int) -> EmployeePass:
        obj = self._service.get_by_id(employee_pass_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        return obj
