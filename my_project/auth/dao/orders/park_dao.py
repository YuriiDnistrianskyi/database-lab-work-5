from typing import List
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain.orders.Park import Park


class ParkDAO(GeneralDAO):
    _domain_type = Park


    def find_by_name(self, name: str) -> List[object]:
        return self._session.query(Park).filter(Park.name == name).all()


    def find_by_location(self, location: str) -> List[object]:
        return self._session.query(Park).filter(Park.location == location).all()
