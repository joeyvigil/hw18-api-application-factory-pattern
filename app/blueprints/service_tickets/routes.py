from app.blueprints.service_tickets import service_tickets_bp
from .schemas import service_ticket_schema, service_tickets_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import ServiceTickets, db


# create service tickets
@service_tickets_bp.route('', methods=['POST']) 
def create_service_ticket():
    try:
        data = service_ticket_schema.load(request.json) # type: ignore
    except ValidationError as e:
        return jsonify(e.messages), 400 
    

    new_service_ticket = ServiceTickets(**data) 
    db.session.add(new_service_ticket)
    db.session.commit()
    return service_ticket_schema.jsonify(new_service_ticket), 201

#Read ServiceTickets
@service_tickets_bp.route('', methods=['GET']) 
def read_service_tickets():
    service_tickets = db.session.query(ServiceTickets).all()
    return service_tickets_schema.jsonify(service_tickets), 200


#Read Individual ServiceTicket - Using a Dynamic Endpoint
@service_tickets_bp.route('<int:service_ticket_id>', methods=['GET'])
def read_service_ticket(service_ticket_id):
    service_ticket = db.session.get(ServiceTickets, service_ticket_id)
    return service_ticket_schema.jsonify(service_ticket), 200


#Delete a ServiceTicket
@service_tickets_bp.route('<int:service_ticket_id>', methods=['DELETE'])
def delete_service_ticket(service_ticket_id):
    service_ticket = db.session.get(ServiceTickets, service_ticket_id)
    db.session.delete(service_ticket)
    db.session.commit()
    return jsonify({"message": f"Successfully deleted service_ticket {service_ticket_id}"}), 200


#Update a ServiceTicket
@service_tickets_bp.route('<int:service_ticket_id>', methods=['PUT'])
def update_service_ticket(service_ticket_id):
    service_ticket = db.session.get(ServiceTickets, service_ticket_id) 

    if not service_ticket: 
        return jsonify({"message": "service_ticket not found"}), 404  
    
    try:
        service_ticket_data = service_ticket_schema.load(request.json)  # type: ignore
    except ValidationError as e:
        return jsonify({"message": e.messages}), 400
    
    for key, value in service_ticket_data.items(): 
        setattr(service_ticket, key, value) 

    db.session.commit()
    return service_ticket_schema.jsonify(service_ticket), 200
    