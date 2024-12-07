from my_project.auth.dao import pass_show_dao
from my_project.auth.domain.orders.pass_show import PassShow
from my_project.auth.service.general_service import GeneralService


class PassShowService(GeneralService):
    _dao = pass_show_dao
    _class_type = PassShow

    def get_by_two_id(self, pass_id: int, show_id: int) -> _dao:
        return self._dao.get_by_two_id(pass_id, show_id)


    def update_by_two_id(self, pass_id: int, show_id: int, obj: _dao):
        self._dao.update_by_two_id(pass_id, show_id, obj)


    def delete_by_two_id(self, pass_id: int, show_id: int,):
        self._dao.delete_by_two_id(pass_id, show_id)
