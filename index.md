
# Artifact One - Device Module From Python/Flask Web Application

[Artifact One - Python/Flask Web Application](https://github.com/thewickk/thewickk.github.io/tree/master/servers)

## Artifact Description:

* This artifact is a modular piece of a Python/Flask web application used to manage and track computer inventory in a home/office setting. This artifact is one piece of a larger application that allows users, via a web interface, to update and modify a PostgreSQL database to keep track of computers, network devices, and IP address to better manage their IT infrastructure. This application was created in May of 2019.

## Justification of Artifact:

* I chose this artifact because I think it fully encompasses the paradigm of Object-Oriented Design. This artifact showcases how the functionality of a program can be separated into smaller modular components that can be linked together via a common interface and added or removed as dictated by the End-User needs. This artifact contains a templates directory which contain all the html pages which provide the user interface to view and input information to perform CRUD operations on the PostgreSQL database. This artifact then relies on four additional Python files to tie the components of this artifact to the application as a whole:

* I. `__init__.py` – This file is defined as a “Blueprint” and allows this module to be called by the application upon initialization. This is a design typical in a Flask application. 
* II. `forms.py` – This Python file is the interface to the database. This is the form that users would POST to the database to Create and Update new and existing computer and network devices present in their home or office
* III. `models.py` – This is the Python file that creates a Class that represents a table entry in the PostgreSQL database. This uses the concept of Object-relational mapping to allow programmatic interaction between the SQL database language and the Python language. In addition to creating tables in the database this concept of Class based models allows, through Flask, relationships between other models that allows the modification of other tables through the relationship established within this model. 
* IV. `routes.py` – This is the file that sets up the routing between the various web pages and their respective functionality. The routes.py model lies at the heart of RESTful architecture and brings the application to the users via the web.

## Reflection:

* Enhancement of this artifact was much more challenging than I originally expected. As there is a lot of functionality specific to the work environment this application was created for, care needs to be taken to remove/revise components to make this a more generic application without breaking the functionality of the overall application. The benefit of this experience is that I really got the opportunity to appreciate the modular concept of Object-Oriented Design. Though many changes need to be made in this artifact to make it more generic, this artifact is only one of ten other modules that make up the application, and thankfully due to the OOD design concept, changes only need to be made in this artifact and will not affect the other modular components. 
