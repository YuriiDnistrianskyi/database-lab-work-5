from typing import List
from my_project.auth.dao import park_dao
from my_project.auth.domain.orders.Park import Park
from my_project.auth.service.general_service import GeneralService

class ParkService(GeneralService):
    _dao = park_dao
    _class_type = Park

    def get_park_by_name(self, name: str) -> List[object]:
        return self._dao.find_by_name(name)

    def get_park_by_location(self, location: str) -> List[object]:
        return self._dao.find_by_location(location)
