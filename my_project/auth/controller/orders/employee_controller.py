from flask import abort
from http import HTTPStatus
from typing import List
from my_project.auth.service import employee_service
from my_project.auth.domain.orders.employee import Employee
from my_project.auth.controller.general_controller import GeneralController

class EmployeeController(GeneralController):
    _service = employee_service

    def find_all(self) -> List[Employee]:
        return self._service.get_all()

    def create_employee(self, employee: Employee) -> None:
        self._service.create(employee)

    def update_employee(self, employee_id: int, employee: Employee) -> None:
        obj = self._service.get_by_id(employee_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.update(employee_id, employee)

    def delete_employee(self, employee_id: int) -> None:
        obj = self._service.get_by_id(employee_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(employee_id)

    def find_employee_by_id(self, employee_id: int) -> Employee:
        obj = self._service.get_by_id(employee_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        return obj
