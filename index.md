
# Artifact One - Device Module From Python/Flask Web Application

Link to Artifact One Module Code:

* [Artifact One - Python/Flask Web Application](https://github.com/thewickk/thewickk.github.io/tree/master/servers)

## Artifact One Description:

* This artifact is a modular piece of a Python/Flask web application used to manage and track computer inventory in a home/office setting. This artifact is one piece of a larger application that allows users, via a web interface, to update and modify a PostgreSQL database to keep track of computers, network devices, and IP address to better manage their IT infrastructure. This application was created in May of 2019.

## Justification of Artifact One:

* I chose this artifact because I think it fully encompasses the paradigm of Object-Oriented Design. This artifact showcases how the functionality of a program can be separated into smaller modular components that can be linked together via a common interface and added or removed as dictated by the End-User needs. This artifact contains a templates directory which contain all the html pages which provide the user interface to view and input information to perform CRUD operations on the PostgreSQL database. This artifact then relies on four additional Python files to tie the components of this artifact to the application as a whole:

* I. `__init__.py` – This file is defined as a “Blueprint” and allows this module to be called by the application upon initialization. This is a design typical in a Flask application. 
* II. `forms.py` – This Python file is the interface to the database. This is the form that users would POST to the database to Create and Update new and existing computer and network devices present in their home or office
* III. `models.py` – This is the Python file that creates a Class that represents a table entry in the PostgreSQL database. This uses the concept of Object-relational mapping to allow programmatic interaction between the SQL database language and the Python language. In addition to creating tables in the database this concept of Class based models allows, through Flask, relationships between other models that allows the modification of other tables through the relationship established within this model. 
* IV. `routes.py` – This is the file that sets up the routing between the various web pages and their respective functionality. The routes.py model lies at the heart of RESTful architecture and brings the application to the users via the web.

## Reflection on Artifact One:

* Enhancement of this artifact was much more challenging than I originally expected. As there is a lot of functionality specific to the work environment this application was created for, care needs to be taken to remove/revise components to make this a more generic application without breaking the functionality of the overall application. The benefit of this experience is that I really got the opportunity to appreciate the modular concept of Object-Oriented Design. Though many changes need to be made in this artifact to make it more generic, this artifact is only one of ten other modules that make up the application, and thankfully due to the OOD design concept, changes only need to be made in this artifact and will not affect the other modular components. 

# Artifact Two - Device Module From Python/Flask Web Application

Link to Artifact One Module Code:

* [Artifact Two - Linux File Scanner written in the C Programming Language](https://github.com/thewickk/thewickk.github.io/tree/master/file_scanner)

## Artifact Two Description:

* Artifact two is a program written in C and can be used as file system scanner on a machine running the Linux Operating System. This program uses a function pointer as a callback to make recursive calls to step through a user provided root path to a directory on their Linux system. The program recurses through the directory structure and prints out the parent and child directories and the files contained within each. This program was originally created in March of 2020.  

## Justification of Artifact Two:

* This program uses user defined data structures to provide the functionality and error checking of this program. It is a unique take on the functionality of the built in Linux functions ‘ls’ and ‘find’. The algorithm that comprises the function is simple, yet showcases my understanding of flow control, conditional statements, recursion, and callback functions. In addition, this program highlights my understanding of how to interact with a POSIX compliant operating system. This artifact has been improved for the original by including a function pointer that acts as a callback to perform the recursive calls to continue to search the directory tree. 

## Reflection on Artifact Two:

* This artifact has been the most fun to enhance. I enjoy programming in C as it lends itself to topics, I am most interested in, Linux, embedded systems, and hardware. Though the algorithm of the file scanner was familiar to me adding the function pointer as a callback function was challenging and took some time to understand. In addition, I learned how to compile this program into a shared library using a Makefile which enhances its portability and allows me to share this module as a library if someone else was interested in using it. 