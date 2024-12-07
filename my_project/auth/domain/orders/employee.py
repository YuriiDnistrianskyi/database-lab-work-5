from __future__ import annotations #
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto

class Employee(db.Model, IDto):
    __tablename__ = 'Employee'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    position_id = db.Column(db.Integer, db.ForeignKey('Position.id', name='fk_employee_position'), nullable=False) # foreign key
    gender_id = db.Column(db.Integer, db.ForeignKey('Gender.id', name='fk_employee_gender'), nullable=False)

    employee_passes = db.relationship('EmployeePass', backref='employee', lazy=True)


    def __repr__(self) -> str:
        return (f"Employee({self.id}, "
                f"'{self.first_name}', "
                f"'{self.last_name}')', "
                f"{self.position_id}, "
                f"{self.gender_id})"
                )


    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "position": self.position.put_into_dto() if self.position else None,
            "gender": self.gender.put_into_dto() if self.gender else None,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Employee:
        return Employee(**dto_dict)

