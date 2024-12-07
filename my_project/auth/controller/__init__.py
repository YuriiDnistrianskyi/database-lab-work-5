from .orders.park_controller import ParkController
from .orders.attraction_controller import AttractionController
from .orders.show_event_controller import ShowEventController
from .orders.employee_controller import EmployeeController
from .orders.actor_controller import ActorController
from .orders.client_controller import ClientController
from .orders.ticket_controller import TicketController
from .orders.employee_pass_controller import EmployeePassController
from .orders.actor_pass_controller import ActorPassController
from .orders.gender_controller import GenderController
from .orders.position_controller import PositionController
from .orders.park_attraction_controller import ParkAttractionController
from .orders.park_show_controller import ParkShowController
from .orders.park_ticket_controller import ParkTicketController
from .orders.pass_attraction_controller import PassAttractionController
from .orders.pass_show_controller import PassShowController
from .orders.park_employee_controller import ParkEmployeeController

from .procedures.procedure_price_controller import ProcedurePriceController
from .procedures.insert_in_position_controller import InsertInPositionController
from .procedures.procedure_park_employee_controller import ProcedureParkEmployeeController
from .procedures.create_random_tables_controller import CreateRandomTablesController

park_controller = ParkController()
attraction_controller = AttractionController()
show_event_controller = ShowEventController()
employee_controller = EmployeeController()
actor_controller = ActorController()
client_controller = ClientController()
ticket_controller = TicketController()
employee_pass_controller = EmployeePassController()
actor_pass_controller = ActorPassController()
gender_controller = GenderController()
position_controller = PositionController()
park_attraction_controller = ParkAttractionController()
park_show_controller = ParkShowController()
park_ticket_controller = ParkTicketController()
pass_attraction_controller = PassAttractionController()
pass_show_controller = PassShowController()
park_employee_controller = ParkEmployeeController()

procedure_price_controller = ProcedurePriceController()
insert_in_position_controller = InsertInPositionController()
procedure_park_employee_controller = ProcedureParkEmployeeController()
create_random_tables_controller = CreateRandomTablesController()
