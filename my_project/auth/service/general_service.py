"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from abc import ABC
from typing import List


class GeneralService(ABC):
    _dao = None
    _class_type = None

    def create(self, obj: _class_type) -> None:
        self._dao.create(obj)


    def update(self, obj_id: int, obj: _class_type) -> None:
        self._dao.update(obj_id, obj)


    def get_all(self) -> List[_class_type]:
        return self._dao.find_all()


    def get_by_id(self, obj_id: int) -> _class_type:
        return self._dao.find_by_id(obj_id)


    def delete(self, key: int) -> None:
        self._dao.delete(key)
