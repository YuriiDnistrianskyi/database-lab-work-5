from .orders.park_service import ParkService
from .orders.attraction_service import AttractionService
from .orders.show_event_service import ShowEventService
from .orders.employee_service import EmployeeService
from .orders.actor_service import ActorService
from .orders.client_service import ClientService
from .orders.ticket_service import TicketService
from .orders.employee_pass_service import EmployeePassService
from .orders.actor_pass_service import ActorPassService
from .orders.gender_service import GenderService
from .orders.position_service import PositionService
from .orders.park_attraction_service import ParkAttractionService
from .orders.park_show_service import ParkShowService
from .orders.park_ticket_service import ParkTicketService
from .orders.pass_attraction_service import PassAttractionService
from .orders.pass_show_service import PassShowService
from .orders.park_employee_service import ParkEmployeeService


park_service = ParkService()
attraction_service = AttractionService()
show_event_service = ShowEventService()
employee_service = EmployeeService()
actor_service = ActorService()
client_service = ClientService()
ticket_service = TicketService()
employee_pass_service = EmployeePassService()
actor_pass_service = ActorPassService()
gender_service = GenderService()
position_service = PositionService()
park_attraction_service = ParkAttractionService()
park_show_service = ParkShowService()
park_ticket_service = ParkTicketService()
pass_attraction_service = PassAttractionService()
pass_show_service = PassShowService()
park_employee_service = ParkEmployeeService()
