from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class ShowEvent(db.Model, IDto):
    __tablename__ = 'ShowEvent'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    time = db.Column(db.Integer, nullable=False)
    actors = db.Column(db.Integer, nullable=False)


    def __repr__(self) -> str:
        return f"ShowEvent({self.id}, '{self.name}', {self.time}, {self.actors})"


    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "name": self.name,
            "time": self.time,
            "actors": self.actors,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ShowEvent:
        return ShowEvent(**dto_dict)
