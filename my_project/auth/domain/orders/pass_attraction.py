from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class PassAttraction(db.Model, IDto):
    __tablename__ = 'PassAttraction'


    pass_id = db.Column(db.Integer, db.ForeignKey('EmployeePass.id', name='fk_pass_attraction_pass'), primary_key=True)
    attraction_id = db.Column(db.Integer, db.ForeignKey('Attraction.id', name='fk_pass_attraction_attraction'), primary_key=True)


    def __repr__(self) -> str:
        return f"PassAttraction({self.pass_id}, {self.attraction_id})"


    def put_into_dto(self) -> Dict[str, object]:
        return {
            "pass_id": self.pass_id,
            "attraction_id": self.attraction_id,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PassAttraction:
        return PassAttraction(**dto_dict)
