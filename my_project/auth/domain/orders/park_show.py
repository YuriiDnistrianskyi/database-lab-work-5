from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class ParkShow(db.Model, IDto):
    __tablename__ = 'ParkShow'

    park_id = db.Column(db.Integer, db.ForeignKey('Park.id', name='fk_park_show_park'), primary_key=True)
    show_id = db.Column(db.Integer, db.ForeignKey('ShowEvent.id', name='fk_park_show_show'), primary_key=True)


    def __repr__(self) -> str:
        return f"ParkShow({self.park_id}, {self.show_id})"


    def put_into_dto(self) -> Dict[str, object]:
        return {
            "park_id": self.park_id,
            "show_id": self.show_id,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ParkShow:
        return ParkShow(**dto_dict)
