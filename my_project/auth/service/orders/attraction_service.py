from typing import List
from my_project.auth.dao import attraction_dao
from my_project.auth.domain.orders.attraction import Attraction
from my_project.auth.service.general_service import GeneralService


class AttractionService(GeneralService):
    _dao = attraction_dao
    _class_type = Attraction


    """def create(self, attraction: Attraction) -> None:
        self._dao.create(attraction)


    def update(self, attraction_id: int, attraction: Attraction) -> None:
        self._dao.update(attraction_id, attraction) #розібрати


    def get_all(self) -> List[Attraction]:
        return self._dao.find_all()


    def get_by_id(self, attraction_id: int) -> Attraction:
        return self._dao.find_by_id(attraction_id)"""


    def get_by_name(self, name: str) -> List[object]:
        return self._dao.find_by_name(name)


    def get_by_capacity(self, capacity: int) -> List[Attraction]:
        return self._dao.find_by_capacity(capacity)
