from my_project.auth.dao import employee_pass_dao
from my_project.auth.domain.orders.employee_pass import EmployeePass
from my_project.auth.service.general_service import GeneralService


class EmployeePassService(GeneralService):
    _dao = employee_pass_dao
    _class_type = EmployeePass
