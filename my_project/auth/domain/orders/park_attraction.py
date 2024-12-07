from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class ParkAttraction(db.Model, IDto):
    __tablename__ = 'ParkAttraction'

    park_id = db.Column(db.Integer, db.ForeignKey('Park.id', name='fk_park_attraction_park'), primary_key=True)
    attraction_id = db.Column(db.Integer, db.ForeignKey('Attraction.id', name='fk_park_attraction_attraction'), primary_key=True)


    def __repr__(self) -> str:
        return f"ParkAttraction({self.park_id}, {self.attraction_id})"


    def put_into_dto(self) -> Dict[str, object]:
        return {
            "park_id": self.park_id,
            "attraction_id": self.attraction_id,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ParkAttraction:
        return ParkAttraction(**dto_dict)
