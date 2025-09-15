from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Park(db.Model, IDto):
    __tablename__ = 'Park'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    location = db.Column(db.String(100))
    maxVisit = db.Column(db.Integer)
    attractionNumber = db.Column(db.Integer)
    age = db.Column(db.Integer)


    def __repr__(self) -> str:
        return (f"Park({self.id}, "
                f"'{self.name}', "
                f"'{self.location}', "
                f"'{self.maxVisit}', "
                f"'{self.attractionNumber}', "
                f"'{self.age}')")


    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "location": self.location,
            "maxVisit": self.maxVisit,
            "attractionNumber": self.attractionNumber,
            "Age": self.age
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Park:
        return Park(**dto_dict)

