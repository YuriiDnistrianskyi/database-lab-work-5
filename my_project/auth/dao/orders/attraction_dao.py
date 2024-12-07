from typing import List
from my_project.auth.dao.general_dao import GeneralDAO #
from my_project.auth.domain.orders.attraction import Attraction


class AttractionDAO(GeneralDAO):
    _domain_type = Attraction

    def find_by_name(self, name: str) -> List[object]:
        return self._session.query(Attraction).filter(Attraction.name == name).all()

    def find_by_capacity(self, capacity: int) -> List[object]:
        return self._session.query(Attraction).filter(Attraction.capacity == capacity).all()

