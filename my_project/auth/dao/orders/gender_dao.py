from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.gender import Gender


class GenderDAO(GeneralDAO):
    _domain_type = Gender
