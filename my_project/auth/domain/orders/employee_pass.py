from __future__ import annotations
from typing import Dict, Any

import app

from my_project import db
from my_project.auth.domain.i_dto import IDto

class EmployeePass(db.Model, IDto):
    __tablename__ = 'EmployeePass'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('Employee.id', name='fk_employee_pass'), nullable=False)
    date_of_issue = db.Column(db.Date, nullable=False)
    date_of_expire = db.Column(db.Date, nullable=False)



    def __repr__(self) -> str:
        return f"EmployeePass({self.id}, {self.employee_id}, {self.date_of_issue}, {self.date_of_expire})"


    def put_into_dto(self) -> Dict[str, object]:
        return {
            "id": self.id,
            "employee_id": self.employee.put_into_dto() if self.employee else None,
            "date_of_issue": self.date_of_issue,
            "date_of_expire": self.date_of_expire,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> EmployeePass:
        return EmployeePass(**dto_dict)

