from .orders.park_dao import ParkDAO
from .orders.attraction_dao import AttractionDAO
from .orders.show_event_dao import ShowEventDAO
from .orders.employee_dao import EmployeeDAO
from .orders.actor_dao import ActorDAO
from .orders.client_dao import ClientDAO
from .orders.ticket_dao import TicketDAO
from .orders.employee_pass_dao import EmployeePassDAO
from .orders.actor_pass_dao import ActorPassDAO
from .orders.gender_dao import GenderDAO
from .orders.position_dao import PositionDAO
from .orders.park_attraction_dao import ParkAttractionDAO
from .orders.park_show_dao import  ParkShowDAO
from .orders.park_ticket_dao import ParkTicketDAO
from .orders.pass_attraction_dao import PassAttractionDAO
from .orders.pass_show_dao import PassShowDAO
from .orders.park_employee_dao import ParkEmployeeDAO


park_dao = ParkDAO()
attraction_dao = AttractionDAO()
show_event_dao = ShowEventDAO()
employee_dao = EmployeeDAO()
actor_dao = ActorDAO()
client_dao = ClientDAO()
ticket_dao = TicketDAO()
employee_pass_dao = EmployeePassDAO()
actor_pass_dao = ActorPassDAO()
gender_dao = GenderDAO()
position_dao = PositionDAO()
park_attraction_dao = ParkAttractionDAO()
park_show_dao = ParkShowDAO()
park_ticket_dao = ParkTicketDAO()
pass_attraction_dao = PassAttractionDAO()
pass_show_dao = PassShowDAO()
park_employee_dao = ParkEmployeeDAO()


