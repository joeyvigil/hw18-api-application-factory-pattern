from app.extensions import ma
from app.models import ServiceTickets, db


class ServiceTicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceTickets #Creates a schema that validates the data as defined by our ServiceTickets Model

service_ticket_schema = ServiceTicketSchema() 
service_tickets_schema = ServiceTicketSchema(many=True) #Allows this schema to translate a list of ServiceTicket objects all at once
