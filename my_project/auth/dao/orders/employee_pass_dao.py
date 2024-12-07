from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.employee_pass import EmployeePass


class EmployeePassDAO(GeneralDAO):
    _domain_type = EmployeePass
