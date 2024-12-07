"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from abc import ABC
from typing import List

from sqlalchemy import inspect
from sqlalchemy.orm import Mapper

from my_project import db


class GeneralDAO(ABC):
    _domain_type = None
    _session = db.session

    def create(self, obj: _domain_type) -> None:
        self._session.add(obj)
        self._session.commit()


    def find_all(self) -> List[_domain_type]:
        return self._session.query(self._domain_type)


    def find_by_id(self, obj_id: int) -> _domain_type:
        return self._session.query(self._domain_type).filter(self._domain_type.id == obj_id).first()

    # ----------- #
    def update(self, obj_id: int, in_obj: object) -> None:
        domain_obj = self._session.query(self._domain_type).get(obj_id) #
        mapper: Mapper = inspect(type(in_obj))  # Metadata
        columns = mapper.columns._collection
        for column_name, column_obj, *_ in columns:
            if not column_obj.primary_key:
                value = getattr(in_obj, column_name)
                setattr(domain_obj, column_name, value)
        self._session.commit()


    def delete(self, obj_id: int) -> None:
        domain_obj = self._session.query(self._domain_type).get(obj_id)
        self._session.delete(domain_obj)
        try:
            self._session.commit()
        except Exception:
            self._session.rollback()
            raise
