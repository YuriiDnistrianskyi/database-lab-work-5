from __future__ import annotations #
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Attraction(db.Model, IDto):
    __tablename__ = 'Attraction'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False) #
    capacity = db.Column(db.Integer, nullable=False)
    ticketBooking = db.Column(db.Boolean, nullable=False)


    def __repr__(self) -> str:
        return (f"Attraction {self.id}, "
                f"'{self.name}', "
                f"'{self.capacity}', " 
                f"'{self.ticketBooking}')"
                )


    def put_into_dto(self) -> Dict[str, Any]: #
        return {
            "id": self.id,
            "name": self.name,
            "capacity": self.capacity,
            "tickedBooking": self.ticketBooking
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Attraction:
        return Attraction(**dto_dict) #

