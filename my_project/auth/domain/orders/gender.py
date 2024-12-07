from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Gender(db.Model, IDto):
    __tablename__ = 'Gender'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)

    employees = db.relationship('Employee', backref='gender', lazy=True)


    def __repr__(self) -> str:
        return f"Gender({self.id}, '{self.title}')"


    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "title": self.title
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Gender:
        return Gender(**dto_dict)