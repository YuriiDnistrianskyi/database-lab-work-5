from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class ActorPass(db.Model, IDto):
    __tablename__ = 'ActorPass'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    actor_id = db.Column(db.Integer, db.ForeignKey('Actor.id', name='fk_actor_pass'), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    date_of_issue = db.Column(db.Date, nullable=False)
    date_of_expire = db.Column(db.Date, nullable=False)


    def __repr__(self) -> str:
        return f"ActorPass({self.id}, {self.actor_id}, '{self.role}', {self.date_of_issue}, {self.date_of_expire})"


    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "actor_id": self.actor_id,
            "role": self.role,
            "date_of_issue": self.date_of_issue,
            "date_of_expire": self.date_of_expire,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ActorPass:
        return ActorPass(**dto_dict)
