from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Ticket(db.Model, IDto):
    __tablename__ = 'Ticket'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer, db.ForeignKey('Client.id', name='fk_ticket_owner'))
    date = db.Column(db.Date, nullable=False)
    line_free = db.Column(db.Boolean, nullable=False)
    price = db.Column(db.Integer, nullable=False)


    def __repr__(self) -> str:
        return f"Ticket({self.id}, {self.client_id}, {self.date}, {self.line_free}, {self.price})"


    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "owner_id": self.client_id,
            "date": self.date,
            "line_free": self.line_free,
            "price": self.price,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Ticket:
        return Ticket(**dto_dict)
