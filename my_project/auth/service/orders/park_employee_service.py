from my_project.auth.dao import park_employee_dao
from my_project.auth.domain.orders.park_employee import ParkEmployee
from my_project.auth.service.general_service import GeneralService


class ParkEmployeeService(GeneralService):
    _dao = park_employee_dao
    _class_type = ParkEmployee

    def get_by_two_id(self, park_id: int, employee_id: int) -> _dao:
        return self._dao.get_by_two_id(park_id, employee_id)


    def update_by_two_id(self, park_id: int, employee_id: int, obj: _dao):
        self._dao.update_by_two_id(park_id, employee_id, obj)


    def delete_by_two_id(self, park_id: int, employee_id: int,):
        self._dao.delete_by_two_id(park_id, employee_id)
