from flask import abort
from typing import List
from http import HTTPStatus
from my_project.auth.service import show_event_service
from my_project.auth.domain.orders.show_event import ShowEvent
from my_project.auth.controller.general_controller import GeneralController


class ShowEventController(GeneralController):
    _service = show_event_service


    def find_all(self) -> List[ShowEvent]:
        return self._service.get_all()


    def create_show_event(self, show_event: ShowEvent) -> None:
        self._service.create(show_event)


    def update_show_event(self, show_event_id: int, show_event: ShowEvent) -> None:
        obj = self._service.get_by_id(show_event_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.update(show_event_id, show_event)


    def delete_show_event(self, show_event_id: int) -> None:
        obj = self._service.get_by_id(show_event_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        self._service.delete(show_event_id)


    def find_show_event_by_id(self, show_event_id: int) -> ShowEvent:
        obj = self._service.get_by_id(show_event_id)
        if not obj:
            abort(HTTPStatus.NOT_FOUND)
        return obj
