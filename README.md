# hw18-api-application-factory-pattern
*Flask project using application factory pattern*

Hopefully at this point you have been following along with each Practice Assignment and should only have a few pieces left to put into place. Everything from those Practice Assignments will be required in this Knowledge check.

```
/project
├── /app
│   ├── __init__.py - create_app() lives here
│   ├── extensions.py
│   ├── /blueprints
│	│	├──/user
│	│	├──__init__.py  - Initialize User Blueprint
│	│	├── routes.py  - Create User Controllers/routes
│	│	└── schemas.py
│   └── models.py
├── app.py
└── config.py
```

## Blueprint:
Create Blueprint folders for mechanic and service ticket. Each Blueprint folder should have the following:

-   **_\_init__.py**: In this file you initialize the blueprint (don't forget to import the routes into this file after the initialization.)
-   **routes.py**: Here is were you create the routes specific to that resource
-   **schemas.py**: This is the file where you define the schemas used to serialize and deserialize data for the routes

After initializing the the blueprints register them in your app/_\_init__.py file, and assign a url prefix. Remember url prefixes should be the plural name of the resource (hint: /mechanics, /service-tickets)

## Marshmallow Schemas:
Define basic Schemas for your mechanic and service_ticket resources. Remember you can take advantage of SQLAlchemyAutoSchema to quickly generate the schema based of the model you created for that particular resource.

## Routes:

*all examples using local host as http://127.0.0.1:5000*

**Mechanic:** Create full CRUD routes for your mechanic resource, and remember you should have a url_prefix set up so a lot of your route endpoints will be '/'.

-   **POST '/'** : Creates a new Mechanic
```json
method: POST 
url: http://127.0.0.1:5000/mechanics
body(raw): 
{
    "address": "1990 W Philly Ave",
    "email": "fun@games.com",
    "first_name": "james",
    "last_name": "thorton",
    "password": "123password",
    "salary": 1000000
}
response: 
{
    "address": "1990 W Philly Ave",
    "email": "fun@games.com",
    "first_name": "james",
    "id": 4,
    "last_name": "thorton",
    "password": "123password",
    "salary": 1000000.0
}
```
-   **GET '/'**: Retrieves all Mechanics
```json
method: GET
url: http://127.0.0.1:5000/mechanics
response:
[
    {
        "address": "123 street",
        "email": "j@v.com",
        "first_name": "joey",
        "id": 1,
        "last_name": "vigil",
        "password": "123-4567",
        "salary": 420.0
    },
    {
        "address": "123 street1",
        "email": "j@v.com1",
        "first_name": "joey1",
        "id": 2,
        "last_name": "vigil1",
        "password": "123-45671",
        "salary": 4201.0
    },
    {
        "address": "123 street12",
        "email": "j@v.com12",
        "first_name": "joey12",
        "id": 3,
        "last_name": "vigil12",
        "password": "123-456712",
        "salary": 42012.0
    },
    {
        "address": "1990 W Philly Ave",
        "email": "fun@games.com",
        "first_name": "james",
        "id": 4,
        "last_name": "thorton",
        "password": "123password",
        "salary": 1000000.0
    }
]
```
-   **PUT '/\<int:id>'**:  Updates a specific Mechanic based on the id passed in through the url.
```json
method: PUT
url: http://127.0.0.1:5000/mechanics/4
Body (raw): 
{
    "address":"",
    "email": "james@brown.com",
    "first_name":"",
    "last_name":"brown",
    "password": "",
    "salary": 999999
}
response:
{
    "address": "1990 W Philly Ave",
    "email": "james@brown.com",
    "first_name": "james",
    "id": 4,
    "last_name": "brown",
    "password": "123password",
    "salary": 999999.0
}
```
-   **DELETE '/\<int:id'>**: Deletes a specific Mechanic based on the id passed in through the url.
```json
method: DELETE
url: http://127.0.0.1:5000/mechanics/3
response:
{
    "message": "Successfully deleted mechanic 3"
}
```

**Service_Ticket:** Create the following routes to Create service tickets, assign mechanics, remove mechanics, and retrieve all service tickets.

-   **POST '/'**: Pass in all the required information to create the service_ticket.
```json
method: POST
url: http://127.0.0.1:5000/service_tickets
body (raw):
{ 
    "customer_id": 2,
    "car_VIM": "VIM123456789",
    "price": 500.25,
    "service_desc": "4x new wheels"
    
}
response:
{
    "car_VIM": "VIM123456789",
    "customer_id": 2,
    "id": 2,
    "price": 500.25,
    "service_date": "2025-08-19",
    "service_desc": "4x new wheels"
}
```
-   **PUT '/\<ticket_id>/assign-mechanic/\<mechanic-id>**: Adds a relationship between a service ticket and the mechanics. (Reminder: use your relationship attributes! They allow you the treat the relationship like a list, able to append a Mechanic to the mechanics list).
```json
method: POST
url: http://127.0.0.1:5000/service_mechanics/2/assign-mechanic/4
response:
{
    "id": 7,
    "mechanic_id": 4,
    "ticket_id": 2
}
```
-   **DELETE '/\<ticket_id>/remove-mechanic/\<mechanic-id>**: Removes the relationship from the service ticket and the mechanic.
```json
method: DELETE
url: http://127.0.0.1:5000/service_mechanics/2/remove-mechanic/4
response:
{
    "message": "Successfully deleted service_mechanic "
}
```
-   **GET '/'**: Retrieves all service tickets.
```json
method: GET
url: http://127.0.0.1:5000/service_tickets
response:
[
    {
        "car_VIM": "VIM2313",
        "customer_id": 1,
        "id": 1,
        "price": 123.23,
        "service_date": "1234-12-12",
        "service_desc": "broken wheel"
    },
    {
        "car_VIM": "VIM123456789",
        "customer_id": 2,
        "id": 2,
        "price": 500.25,
        "service_date": "2025-08-19",
        "service_desc": "4x new wheels"
    }
]
```

## Testing and Postman Collections:
As you continue to build new endpoints, you should be testing each endpoint in Postman to ensure functionality.

*Create a Postman collection to store all of these endpoint tests, export the collection and include it with your work.*

If you are unsure how to create and export a Postman collect watch the video linked below.

## Submitting:
For this assignment and all following, please push your work to github, and submit the link to the github repository.