from my_project.auth.service.general_service import GeneralService
from my_project.auth.dao import gender_dao
from my_project.auth.domain.orders.gender import Gender


class GenderService(GeneralService):
    _dao = gender_dao
    _class_type = Gender
