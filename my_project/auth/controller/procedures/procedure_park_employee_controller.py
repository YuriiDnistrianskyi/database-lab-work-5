from flask import abort
from http import HTTPStatus
from my_project import db

class ProcedureParkEmployeeController:
    def activate_procedure_park_employee(self, park_id: int, employee_id: int) -> None:
        try:
            activate_procedure = f"CALL procedure_park_employee({park_id}, {employee_id});"
            db.session.execute(activate_procedure)
            db.session.commit()
        except Exception as ex:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, str(ex))
