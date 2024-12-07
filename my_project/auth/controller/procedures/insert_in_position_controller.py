from flask import abort
from http import HTTPStatus
from my_project import db

class InsertInPositionController:
    def activate_procedure_insert_in_position(self) -> None:
        try:
            activate_procedure = '''
                CALL insert_in_position();
            '''
            db.session.execute(activate_procedure)
            db.session.commit()
        except Exception as ex:
            abort(HTTPStatus.NOT_FOUND, str(ex))
