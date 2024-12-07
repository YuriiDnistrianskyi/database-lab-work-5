from my_project.auth.dao import pass_attraction_dao
from my_project.auth.domain.orders.pass_attraction import PassAttraction
from my_project.auth.service.general_service import GeneralService


class PassAttractionService(GeneralService):
    _dao = pass_attraction_dao
    _class_type = PassAttraction

    def get_by_two_id(self, pass_id: int, attraction_id: int) -> _dao:
        return self._dao.get_by_two_id(pass_id, attraction_id)


    def update_by_two_id(self, pass_id: int, attraction_id: int, obj: _dao):
        self._dao.update_by_two_id(pass_id, attraction_id, obj)


    def delete_by_two_id(self, pass_id: int, attraction_id: int,):
        self._dao.delete_by_two_id(pass_id, attraction_id)
