from typing import List
from my_project.auth.dao import employee_dao
from my_project.auth.domain.orders.employee import Employee
from my_project.auth.service.general_service import GeneralService


class EmployeeService(GeneralService):
    _dao = employee_dao
    _class_type = Employee


    def get_by_first_name(self, first_name: str) -> List[_class_type]:
        return self._dao.find_by_first_name(first_name)


    def get_by_last_name(self, last_name: str) -> List[_class_type]:
        return self._dao.find_by_last_name(last_name)
