"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask
from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:

    app.register_blueprint(err_handler_bp)

    from .orders.park_route import park_bp
    from .orders.attraction_route import attraction_bp
    from .orders.show_event_route import show_event_bp
    from .orders.employee_route import employee_bp
    from .orders.actor_route import actor_bp
    from .orders.client_route import client_bp
    from .orders.ticket_route import ticket_bp
    from .orders.employee_pass_route import employee_pass_bp
    from .orders.actor_pass_route import actor_pass_bp
    from .orders.gender_route import gender_bp
    from .orders.position_route import position_bp
    from .orders.park_attraction_route import park_attraction_bp
    from .orders.park_show_route import park_show_bp
    from .orders.park_ticket_route import park_ticket_bp
    from .orders.pass_attraction_route import pass_attraction_bp
    from .orders.pass_show_route import pass_show_bp
    from .orders.park_employee_route import park_employee_bp

    from .procedures.procedure_price_route import procedure_price_bp
    from .procedures.insert_in_position_route import insert_in_position_bp
    from .procedures.procedure_park_employee_route import procedure_park_employee_bp
    from .procedures.create_random_tables_route import create_random_tables_bp

    from my_project.auth.auth.routes import auth_bp

    app.register_blueprint(park_bp)
    app.register_blueprint(attraction_bp)
    app.register_blueprint(show_event_bp)
    app.register_blueprint(employee_bp)
    app.register_blueprint(actor_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(ticket_bp)
    app.register_blueprint(employee_pass_bp)
    app.register_blueprint(actor_pass_bp)
    app.register_blueprint(gender_bp)
    app.register_blueprint(position_bp)
    app.register_blueprint(park_attraction_bp)
    app.register_blueprint(park_show_bp)
    app.register_blueprint(park_ticket_bp)
    app.register_blueprint(pass_attraction_bp)
    app.register_blueprint(pass_show_bp)
    app.register_blueprint(park_employee_bp)

    app.register_blueprint(procedure_price_bp)
    app.register_blueprint(insert_in_position_bp)
    app.register_blueprint(procedure_park_employee_bp)
    app.register_blueprint(create_random_tables_bp)

    app.register_blueprint(auth_bp)
