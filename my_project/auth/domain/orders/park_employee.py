from __future__ import annotations #
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class ParkEmployee(db.Model, IDto):
    __tablename__ = 'ParkEmployee'

    park_id = db.Column(db.Integer, db.ForeignKey('Park.id'), primary_key=True, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('Employee.id'), primary_key=True, nullable=False)
    info = db.Column(db.String(50), nullable=False)

    park = db.relationship('Park', backref='ParkEmployee', lazy=True)
    employee = db.relationship('Employee', backref='ParkEmployee', lazy=True)


    def __repr__(self) -> str:
        return f"ParkEmployee('{self.park_id}', '{self.employee_id}', '{self.info}')"


    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "park_id": self.park.put_into_dto() if self.park else None,
            "employee_id": self.employee.put_into_dto() if self.employee else None,
            "info": self.info
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ParkEmployee:
        return ParkEmployee(**dto_dict)
