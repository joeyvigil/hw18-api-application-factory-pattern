from app.extensions import ma
from app.models import ServiceMechanics, db


class ServiceMechanicSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ServiceMechanics 
        include_fk=True

service_mechanic_schema = ServiceMechanicSchema() 
service_mechanics_schema = ServiceMechanicSchema(many=True) #Allows this schema to translate a list of ServiceMechanic objects all at once
