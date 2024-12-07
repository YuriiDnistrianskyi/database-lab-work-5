from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class ParkTicket(db.Model, IDto):
    __tablename__ = 'ParkTicket'

    park_id = db.Column(db.Integer, db.ForeignKey('Park.id', name='fk_park_ticket_park'), primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('Ticket.id', name='fk_park_ticket_ticket'), primary_key=True)


    def __repr__(self) -> str:
        return f"ParkTicket({self.park_id}, {self.ticket_id})"


    def put_into_dto(self) -> Dict[str, object]:
        return {
            "park_id": self.park_id,
            "ticket_id": self.ticket_id,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ParkTicket:
        return ParkTicket(**dto_dict)
