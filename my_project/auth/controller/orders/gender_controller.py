from typing import List
from my_project.auth.service import gender_service
from my_project.auth.domain.orders.gender import Gender
from my_project.auth.controller.general_controller import GeneralController

class GenderController(GeneralController):
    _service = gender_service

    def create_gender(self, gender: Gender) -> None:
        self._service.create(gender) #


    def update_gender(self, gender_id: int, gender: Gender) -> None:
        self._service.update(gender_id, gender)


    def delete_gender(self, gender_id: int) -> None:
        self._service.delete(gender_id)


    def find_all(self) -> List[Gender]:
        return self._service.get_all() #


    def find_gender_by_id(self, gender_id: int) -> Gender:
        return self._service.get_by_id(gender_id)
