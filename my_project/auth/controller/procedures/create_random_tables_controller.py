from flask import abort
from http import HTTPStatus
from my_project import db

class CreateRandomTablesController:
    def activate_procedure_create_random_tables(self) -> None:
        try:
            activate_procedure = '''
                CALL create_random_tables();
            '''
            db.session.execute(activate_procedure)
            db.session.commit()
        except Exception as ex:
            abort(HTTPStatus.NOT_FOUND, str(ex))
