from typing import List
from my_project.auth.dao.general_dao import GeneralDAO #
from my_project.auth.domain.orders.employee import Employee


class EmployeeDAO(GeneralDAO):
    _domain_type = Employee
    _class_type = Employee

    def find_by_first_name(self, first_name: str) -> List[object]:
        return self._session.query(Employee).filter(Employee.first_name == first_name).all()


    def find_by_last_name(self, last_name: str) -> List[object]:
        return self._session.query(Employee).filter(Employee.last_name == last_name).all()
