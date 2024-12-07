from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class PassShow(db.Model, IDto):
    __tablename__ = 'PassShow'


    pass_id = db.Column(db.Integer, db.ForeignKey('ActorPass.id', name='fk_pass_show_pass'), primary_key=True)
    show_id = db.Column(db.Integer, db.ForeignKey('ShowEvent.id', name='fk_pass_show_show'), primary_key=True)


    def __repr__(self) -> str:
        return f"PassShow({self.pass_id}, {self.show_id})"


    def put_into_dto(self) -> Dict[str, object]:
        return {
            "pass_id": self.pass_id,
            "show_id": self.show_id,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> PassShow:
        return PassShow(**dto_dict)
