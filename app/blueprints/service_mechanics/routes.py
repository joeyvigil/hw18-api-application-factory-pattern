from app.blueprints.service_mechanics import service_mechanics_bp
from .schemas import service_mechanic_schema, service_mechanics_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import ServiceMechanics, db


# create service mechanic
@service_mechanics_bp.route('', methods=['POST']) 
def create_service_mechanic():
    try:
        data = service_mechanic_schema.load(request.json) # type: ignore
    except ValidationError as e:
        return jsonify(e.messages), 400 
    

    new_service_mechanic = ServiceMechanics(**data)
    db.session.add(new_service_mechanic)
    db.session.commit()
    return service_mechanic_schema.jsonify(new_service_mechanic), 201

# return all service mechanics
@service_mechanics_bp.route('', methods=['GET']) 
def read_service_mechanics():
    service_mechanics = db.session.query(ServiceMechanics).all()
    return service_mechanics_schema.jsonify(service_mechanics), 200


# return service mechanic at given id
@service_mechanics_bp.route('<int:service_mechanic_id>', methods=['GET'])
def read_service_mechanic(service_mechanic_id):
    service_mechanic = db.session.get(ServiceMechanics, service_mechanic_id)
    return service_mechanic_schema.jsonify(service_mechanic), 200


# delete service mechanic
@service_mechanics_bp.route('<int:service_mechanic_id>', methods=['DELETE'])
def delete_service_mechanic(service_mechanic_id):
    service_mechanic = db.session.get(ServiceMechanics, service_mechanic_id)
    db.session.delete(service_mechanic)
    db.session.commit()
    return jsonify({"message": f"Successfully deleted service_mechanic {service_mechanic_id}"}), 200


# update service mechanic at given id
@service_mechanics_bp.route('<int:service_mechanic_id>', methods=['PUT'])
def update_service_mechanic(service_mechanic_id):
    service_mechanic = db.session.get(ServiceMechanics, service_mechanic_id) 

    if not service_mechanic: 
        return jsonify({"message": "service_mechanic not found"}), 404  
    
    try:
        service_mechanic_data = service_mechanic_schema.load(request.json)  # type: ignore
    except ValidationError as e:
        return jsonify({"message": e.messages}), 400
    
    for key, value in service_mechanic_data.items(): 
        setattr(service_mechanic, key, value) 

    db.session.commit()
    return service_mechanic_schema.jsonify(service_mechanic), 200
    
