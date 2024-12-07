from typing import List
from flask import abort
from http import HTTPStatus
from my_project import db


class ProcedurePriceController:
    def activate_procedure_price(self, ops: str) -> List:
        try:
            data = db.session.execute(f"CALL procedure_price('{ops}');")
            result = [dict(row) for row in data]
            return result
        except Exception as ex:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, str(ex))
