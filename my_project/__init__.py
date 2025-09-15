"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

import os
from http import HTTPStatus
import secrets
from typing import Dict, Any

from flask import Flask
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from flask_jwt_extended import JWTManager

from my_project.auth.route import register_routes

SECRET_KEY = "SECRET_KEY"
SQLALCHEMY_DATABASE_URI = "SQLALCHEMY_DATABASE_URI"
MYSQL_ROOT_USER = "MYSQL_ROOT_USER"
MYSQL_ROOT_PASSWORD = "MYSQL_ROOT_PASSWORD"

# Database
db = SQLAlchemy()

todos = {}


def create_app(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> Flask:
    """
    Creates Flask application
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    :return: Flask application object
    """
    _process_input_config(app_config, additional_config)
    app = Flask(__name__)
    app.config["SECRET_KEY"] = secrets.token_hex(16)
    app.config = {**app.config, **app_config}

    jwt = JWTManager(app)

    _init_db(app)
    register_routes(app)
    _init_swagger(app)

    create_triggers(app)
    create_functions(app)
    create_procedures(app)

    return app


def create_triggers(app: Flask) -> None:
    with app.app_context():
        before_employee_pass_insert = '''
            DROP TRIGGER IF EXISTS before_employeepass_insert;
            CREATE TRIGGER before_employeepass_insert
            BEFORE INSERT
            ON EmployeePass
            FOR EACH ROW
            BEGIN
                IF NOT EXISTS (SELECT 1 FROM employee WHERE employee.id = NEW.employee_id) THEN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Employee is not test  test test found';
                END IF;
            END;
        '''

        before_employee_pass_update = '''
            DROP TRIGGER IF EXISTS before_employee_pass_update;
            CREATE TRIGGER before_employee_pass_update
            BEFORE UPDATE
            ON EmployeePass
            FOR EACH ROW
            BEGIN
                IF NOT EXISTS (SELECT 1 FROM employee WHERE employee.id = NEW.employee_id) THEN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Employee is not found';
                END IF;
            END;
        '''

        before_park_insert = '''
            DROP TRIGGER IF EXISTS before_park_insert; 
            CREATE TRIGGER before_park_update
            BEFORE INSERT
            ON park
            FOR EACH ROW
            BEGIN
                IF EXISTS (SELECT 1 FROM Park WHERE park.name = NEW.name) THEN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Park name exists in table';
                END IF;
            END;
        '''

        before_gender_insert = '''
            DROP TRIGGER IF EXISTS before_gender_insert;
            CREATE TRIGGER before_gender_insert
            BEFORE INSERT
            ON Gender
            FOR EACH ROW
            BEGIN
                IF (SELECT COUNT(*) FROM gender) >= 2 THEN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Gender table have 2 rows';
                END IF;
            END;
        '''


        before_actor_pass_insert = '''
            DROP TRIGGER IF EXISTS before_actor_pass_insert;
            CREATE TRIGGER before_actor_pass_insert
            BEFORE INSERT
            ON ActorPass
            FOR EACH ROW
            BEGIN
                IF (NEW.date_of_issue >= NEW.date_of_expire) THEN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Date of issue > date of expire';
                END IF;
            END;
        '''


        db.session.execute(before_employee_pass_insert)
        db.session.execute(before_employee_pass_update)
        db.session.execute(before_park_insert)
        db.session.execute(before_gender_insert)
        db.session.execute(before_actor_pass_insert)
        db.session.commit()


def create_functions(app: Flask) -> None:
    with app.app_context():
        function_price = '''
            DROP FUNCTION IF EXISTS function_price;
            CREATE FUNCTION function_price(ops VARCHAR(50))
            RETURNS INT
            DETERMINISTIC
            BEGIN
                DECLARE result INT;
                IF (ops = 'sum') THEN
                    SELECT SUM(price) INTO result FROM ticket;
                ELSEIF (ops = 'min') THEN
                    SELECT MIN(price) INTO result FROM ticket;
                ELSEIF (ops = 'max') THEN
                    SELECT MAX(price) INTO result FROM ticket;
                ELSEIF (ops = 'avg') THEN
                    SELECT AVG(price) INTO result FROM ticket;
                ELSE
                    SET result = NULL;
                END IF;
                RETURN result;
            END;                
        '''

        db.session.execute(function_price)
        db.session.commit()


def create_procedures(app: Flask) -> None:
    with app.app_context():
        param_insert_park = '''
            DROP PROCEDURE IF EXISTS param_insert_park;
            CREATE PROCEDURE param_insert_park(name VARCHAR(50), location VARCHAR(50), maxVisit INT, attractionNumber INT, age INT)
            BEGIN
                PREPARE request FROM  "INSERT INTO park (name, location, maxVisit, attractionNumber, age) VALUES (?, ?, ?, ?, ?);";
                SET @name_ = name;
                SET @location_ = location;
                SET @maxVisit_ = maxVisit;
                SET @attractionNumber_ = attractionNumber;
                SET @age_ = age;
                
                EXECUTE request USING @name_, @location_, @maxVisit_, @attractionNumber_, @age_;
                DEALLOCATE PREPARE request;
            END;
        '''

        procedure_price = '''
            DROP PROCEDURE IF EXISTS procedure_price;
            CREATE PROCEDURE procedure_price(ops VARCHAR(50))
            BEGIN
                SELECT function_price(ops);
            END;
        '''

        insert_in_position = '''
            DROP PROCEDURE IF EXISTS insert_in_position;
            CREATE PROCEDURE insert_in_position()
            BEGIN
                DECLARE n INT DEFAULT 1;
                WHILE n <= 10 DO
                    INSERT INTO position (title) VALUES (CONCAT('Position', n));
                    SET n = n + 1;
                END WHILE;
            END;
        '''

        procedure_park_employee = '''
            DROP PROCEDURE IF EXISTS procedure_park_employee;
            CREATE PROCEDURE procedure_park_employee(park_id INT, employee_id INT)
            BEGIN
                DECLARE park_name VARCHAR(50);
                DECLARE employee_name VARCHAR(50);
            
                IF NOT EXISTS (SELECT 1 FROM park WHERE park.id = park_id) THEN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Park not found';
                ELSEIF NOT EXISTS (SELECT 1 FROM employee WHERE id = employee_id) THEN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Employee not found';
                ELSE
                    SELECT name INTO park_name FROM park WHERE park.id = park_id;
                    SELECT CONCAT(last_name, " ", first_name) INTO employee_name FROM employee WHERE employee.id = employee_id;
                    
                    INSERT INTO ParkEmployee (park_id, employee_id, info) VALUES (park_id, employee_id, CONCAT(park_name, ' <- ', employee_name));
                END IF;
            END;
        '''

        create_random_tables = '''
            DROP PROCEDURE IF EXISTS create_random_tables;
            CREATE PROCEDURE create_random_tables()
            BEGIN
                DECLARE done BOOL DEFAULT FALSE;
                DECLARE park_name VARCHAR(50);
                
                DECLARE cursor1 CURSOR FOR SELECT name FROM park;
                DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
                
                
                OPEN cursor1;
                
                read_loop: LOOP
                    FETCH cursor1 INTO park_name;
                
                    IF done THEN
                        LEAVE read_loop;
                    END IF;
                    
                    
                    SET @table_name = CONCAT(park_name, '_', DATE_FORMAT(NOW(), '%Y%m%d%H%i%s')); #
                    SET @column_count = FLOOR(RAND() * (9 - 1 + 1)) + 1;
                    SET @create_query = CONCAT('CREATE TABLE ', @table_name, ' (');
                    
                    SET @i = 1;
                    column_loop: LOOP
                        IF @i > @column_count THEN
                            LEAVE column_loop;
                        END IF;
                        
                        SET @create_query = CONCAT(@create_query, 'column', @i, ' INT');
                        
                        IF @i < @column_count THEN
                            SET @create_query = CONCAT(@create_query, ', '); 
                        END IF;
                        
                        SET @i = @i + 1;
                    END LOOP;
                    
                    SET @create_query = CONCAT(@create_query, ' );');
                    
                    PREPARE request FROM @create_query;
                    EXECUTE request;
                    DEALLOCATE PREPARE request;
                END LOOP;
                CLOSE cursor1;
            END;
        '''


        db.session.execute(param_insert_park)
        db.session.execute(procedure_price)
        db.session.execute(insert_in_position)
        db.session.execute(procedure_park_employee)
        db.session.execute(create_random_tables)
        db.session.commit()


def _init_swagger(app: Flask) -> None:
    # A-lia Swagger
    restx_api = Api(app, title='Pavelchak test backend',
                    description='A simple backend')  # https://flask-restx.readthedocs.io/

    @restx_api.route('/number/<string:todo_id>')
    class TodoSimple(Resource):
        @staticmethod
        def get(todo_id):
            return todos, 202

        @staticmethod
        def put(todo_id):
            todos[todo_id] = todo_id
            return todos, HTTPStatus.CREATED

    @app.route("/hi")
    def hello_world():
        return todos, HTTPStatus.OK


def _init_db(app: Flask) -> None:
    """
    Initializes DB with SQLAlchemy
    :param app: Flask application object
    """
    db.init_app(app)

    if not database_exists(app.config[SQLALCHEMY_DATABASE_URI]):
        create_database(app.config[SQLALCHEMY_DATABASE_URI])

    import my_project.auth.domain
    with app.app_context():
        db.create_all()


def _process_input_config(app_config: Dict[str, Any], additional_config: Dict[str, Any]) -> None:
    """
    Processes input configuration
    :param app_config: Flask configuration
    :param additional_config: additional configuration
    """
    # Get root username and password
    root_user = os.getenv(MYSQL_ROOT_USER, additional_config[MYSQL_ROOT_USER])
    root_password = os.getenv(MYSQL_ROOT_PASSWORD, additional_config[MYSQL_ROOT_PASSWORD])
    # Set root username and password in app_config
    app_config[SQLALCHEMY_DATABASE_URI] = app_config[SQLALCHEMY_DATABASE_URI].format(root_user, root_password)
    pass
