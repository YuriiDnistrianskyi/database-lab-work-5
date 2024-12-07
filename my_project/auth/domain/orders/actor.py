from __future__ import annotations #
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Actor(db.Model, IDto):
    __tablename__ = 'Actor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    gender_id = db.Column(db.Integer, db.ForeignKey('Gender.id', name='fk_actor_gender'), nullable=False)


    def __repr__(self) -> str:
        return f"Actor({self.id}, '{self.first_name}', '{self.last_name}', {self.gender_id})"


    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "gender_id": self.gender_id,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Actor:
        return Actor(**dto_dict)
