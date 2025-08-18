from app.blueprints.mechanics import mechanics_bp
from .schemas import mechanic_schema, mechanics_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Mechanics, db

# Assignment
# POST '/' : Creates a new Mechanic
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

# Assignment
# GET '/': Retrieves all Mechanics
@mechanics_bp.route('', methods=['GET']) 
def read_mechanics():
    mechanics = db.session.query(Mechanics).all()
    return mechanics_schema.jsonify(mechanics), 200


# GET at id
@mechanics_bp.route('<int:mechanic_id>', methods=['GET'])
def read_mechanic(mechanic_id):
    mechanic = db.session.get(Mechanics, mechanic_id)
    return mechanic_schema.jsonify(mechanic), 200

# Assignment
# DELETE '/<int:id'>: Deletes a specific Mechanic based on the id passed in through the url.
@mechanics_bp.route('<int:mechanic_id>', methods=['DELETE'])
def delete_mechanic(mechanic_id):
    mechanic = db.session.get(Mechanics, mechanic_id)
    db.session.delete(mechanic)
    db.session.commit()
    return jsonify({"message": f"Successfully deleted mechanic {mechanic_id}"}), 200

# Assignment
# PUT '/<int:id>':  Updates a specific Mechanic based on the id passed in through the url.
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
        if value: #blank fields will not be updated
            setattr(mechanic, key, value) 

    db.session.commit()
    return mechanic_schema.jsonify(mechanic), 200
    