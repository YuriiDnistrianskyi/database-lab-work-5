from my_project.auth.dao import park_attraction_dao
from my_project.auth.domain.orders.park_attraction import ParkAttraction
from my_project.auth.service.general_service import GeneralService


class ParkAttractionService(GeneralService):
    _dao = park_attraction_dao
    _class_type = ParkAttraction

    def get_by_two_id(self, park_id: int, attraction_id: int) -> ParkAttraction:
        return self._dao.get_by_two_id(park_id, attraction_id)


    def update_by_two_id(self, park_id: int, attraction_id: int, obj: ParkAttraction):
        self._dao.update_by_two_id(park_id, attraction_id, obj)


    def delete_by_two_id(self, park_id: int, attraction_id: int,):
        self._dao.delete_by_two_id(park_id, attraction_id)
