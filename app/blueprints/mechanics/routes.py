from app.blueprints.mechanics import mechanics_bp
from .schemas import mechanic_schema, mechanics_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Mechanics, db

# create new mechanic
@mechanics_bp.route('', methods=['POST']) 
def create_mechanic():
    try:
        data = mechanic_schema.load(request.json) # type: ignore
    except ValidationError as e:
        return jsonify(e.messages), 400 
    

    new_mechanic = Mechanics(**data) 
    db.session.add(new_mechanic)
    db.session.commit()
    return mechanic_schema.jsonify(new_mechanic), 201

# return new mechanic
@mechanics_bp.route('', methods=['GET']) 
def read_mechanics():
    mechanics = db.session.query(Mechanics).all()
    return mechanics_schema.jsonify(mechanics), 200


# return mechanic with given id
@mechanics_bp.route('<int:mechanic_id>', methods=['GET'])
def read_mechanic(mechanic_id):
    mechanic = db.session.get(Mechanics, mechanic_id)
    return mechanic_schema.jsonify(mechanic), 200


# delete mechanic at given id
@mechanics_bp.route('<int:mechanic_id>', methods=['DELETE'])
def delete_mechanic(mechanic_id):
    mechanic = db.session.get(Mechanics, mechanic_id)
    db.session.delete(mechanic)
    db.session.commit()
    return jsonify({"message": f"Successfully deleted mechanic {mechanic_id}"}), 200


# update mechanic info
@mechanics_bp.route('<int:mechanic_id>', methods=['PUT'])
def update_mechanic(mechanic_id):
    mechanic = db.session.get(Mechanics, mechanic_id) 

    if not mechanic: 
        return jsonify({"message": "mechanic not found"}), 404  
    
    try:
        mechanic_data = mechanic_schema.load(request.json)  # type: ignore
    except ValidationError as e:
        return jsonify({"message": e.messages}), 400
    
    for key, value in mechanic_data.items():
        setattr(mechanic, key, value) 

    db.session.commit()
    return mechanic_schema.jsonify(mechanic), 200
    