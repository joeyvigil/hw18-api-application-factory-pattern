# hw18-api-application-factory-pattern
Flask project using application factory pattern

***

Hopefully at this point you have been following along with each Practice Assignment and should only have a few pieces left to put into place. Everything from those Practice Assignments will be required in this Knowledge check.

**Assignment Continuation**

**Blueprint:**\
Create Blueprint folders for mechanic and service ticket. Each Blueprint folder should have the following:

-   **_\_init__.py**: In this file you initialize the blueprint (don't forget to import the routes into this file after the initialization.)
-   **routes.py**: Here is were you create the routes specific to that resource
-   **schemas.py**: This is the file where you define the schemas used to serialize and deserialize data for the routes

After initializing the the blueprints register them in your app/__init__.py file, and assign a url prefix. Remember url prefixes should be the plural name of the resource (hint: /mechanics, /service-tickets)

**Marshmallow Schemas:**\
Define basic Schemas for your mechanic and service_ticket resources. Remember you can take advantage of SQLAlchemyAutoSchema to quickly generate the schema based of the model you created for that particular resource.

**Routes:**

**Mechanic: **Create full CRUD routes for your mechanic resource, and remember you should have a url_prefix set up so a lot of your route endpoints will be '/'.

-   **POST '/'** : Creates a new Mechanic
-   **GET '/'**: Retrieves all Mechanics
-   **PUT '/\<int:id>'**:  Updates a specific Mechanic

    based on the id passed in through the url.
-   **DELETE '/\<int:id'>**: Deletes a specific Mechanic based on the id passed in through the url.

**Service_Ticket:** Create the following routes to Create service tickets, assign mechanics, remove mechanics, and retrieve all service tickets.

-   **POST '/'**: Pass in all the required information to create the service_ticket.
-   **PUT '/\<ticket_id>/assign-mechanic/\<mechanic-id>**: Adds a relationship between a service ticket and the mechanics. (Reminder: use your relationship attributes! They allow you the treat the relationship like a list, able to append a Mechanic to the mechanics list).
-   **PUT '/\<ticket_id>/remove-mechanic/\<mechanic-id>**: Removes the relationship from the service ticket and the mechanic.
-   **GET '/'**: Retrieves all service tickets.

**Testing and Postman Collections:**\
As you continue to build new endpoints, you should be testing each endpoint in Postman to ensure functionality.

**Create a Postman collection to store all of these endpoint tests, export the collection and include it with your work. **

If you are unsure how to create and export a Postman collect watch the video linked below.

**Submitting:**
For this assignment and all following, please push your work to github, and submit the link to the github repository.