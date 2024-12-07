from my_project.auth.dao import park_show_dao
from my_project.auth.domain.orders.park_show import ParkShow
from my_project.auth.service.general_service import GeneralService


class ParkShowService(GeneralService):
    _dao = park_show_dao
    _class_type = ParkShow

    def get_by_two_id(self, park_id: int, show_id: int) -> _dao:
        return self._dao.get_by_two_id(park_id, show_id)


    def update_by_two_id(self, park_id: int, show_id: int, obj: _dao):
        self._dao.update_by_two_id(park_id, show_id, obj)


    def delete_by_two_id(self, park_id: int, show_id: int,):
        self._dao.delete_by_two_id(park_id, show_id)
