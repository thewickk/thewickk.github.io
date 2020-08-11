
# Capstone Project

## Personal Self-Assessment

* I enrolled in the Computer Science degree program in January of 2018 with two goals:

```
1. To increase my chances for employment in the Computer Science and Technologies field
2. To become a well-rounded software developer
```

* I truly believe these goals have been accomplished. Much of the culmination of the effort I have put into achieving these goals is reflected in this ePortfolio. As you parse this document, you will find pieces of code that have real-world applications representing skills that I have gained in Southern New Hampshire University’s Computer Science degree program. The artifacts in this document highlight my understanding of Object-Oriented Programming and Modular Based Design patterns, concepts of Data Structures and Algorithms, and Database design for Web applications and RESTful APIs. 

* While earning my Bachelor of Science in Compute Science degree I have had the opportunity to work on various projects in collaborative environments using Version Control tools such as Git, EGit, GitHub, and Bitbucket where the fundamental version control skills such as pushing, pulling, merging, and resolving merge conflicts were instilled to be able to work together with many Developers on a project. While much of the focus was to become proficient in the use of version control, these projects also afforded the opportunity to learn the various communication skills necessary to communicate the needs of current and perspective clients to the various members of a Software Development team hired to develop a software application. 

* In the following sections you will find that Artifact One acknowledges my ability to create a modular program based on Object-Oriented design principals, while Artifact Two showcases my understanding of Data Structures and Algorithms to implement logical and efficient pieces of code that can benefit a single application or be used as a stand-alone library that can be used in many programs. Finally, Artifact Three highlights how the concepts of Artifact One and Two can be used in conjunction to create Databases that can be used as the backbone of a web-based application, or work just as well as the backend to any software application requiring the use of a mechanism to store data. 

* In each of these Artifacts, the principles of secure coding have been implemented to ensure that the code minimizes the risk to security exploits, follows programming best practices so the code is written in such a way that the underlying functionality should be apparent to any Developer who may need to contribute, edit, or enhance this code, and the standards of the various programming languages have been followed to conform with that languages requirements to contribute to the Open-Source community.

# Artifact One (Software Design and Engineering) - Python/Flask Web Application Module

Link to Artifact One Code:

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

# Artifact Two (Data Structures and Algorithms) - Linux File Scanner written in the C Programming Language

Link to Artifact Two Code:

* [Artifact Two - Linux File Scanner written in the C Programming Language](https://github.com/thewickk/thewickk.github.io/tree/master/file_scanner)

## Artifact Two Description:

* Artifact two is a program written in C and can be used as file system scanner on a machine running the Linux Operating System. This program uses a function pointer as a callback to make recursive calls to step through a user provided root path to a directory on their Linux system. The program recurses through the directory structure and prints out the parent and child directories and the files contained within each. This program was originally created in March of 2020.  

## Justification of Artifact Two:

* This program uses user defined data structures to provide the functionality and error checking of this program. It is a unique take on the functionality of the built in Linux functions ‘ls’ and ‘find’. The algorithm that comprises the function is simple, yet showcases my understanding of flow control, conditional statements, recursion, and callback functions. In addition, this program highlights my understanding of how to interact with a POSIX compliant operating system. This artifact has been improved for the original by including a function pointer that acts as a callback to perform the recursive calls to continue to search the directory tree. 

## Reflection on Artifact Two:

* This artifact has been the most fun to enhance. I enjoy programming in C as it lends itself to topics, I am most interested in, Linux, embedded systems, and hardware. Though the algorithm of the file scanner was familiar to me adding the function pointer as a callback function was challenging and took some time to understand. In addition, I learned how to compile this program into a shared library using a Makefile which enhances its portability and allows me to share this module as a library if someone else was interested in using it. 

# Artifact Three (Databases) - PostgreSQL, SQLAlchemy, and Flask

Link to Artifact Two Code:

* [Artifact Three - PostgreSQL, SQLAlchemy, and Flask](https://github.com/thewickk/thewickk.github.io/tree/master/networks)

## Artifact Three Description:

* This artifact is a modular piece of a Python-Flask web application used to manage and track computer inventory in a home/office setting. This artifact is one piece of a larger application that allows users, via a web interface, to update and modify a PostgreSQL database to keep track of computers, network devices, and IP address to better manage their IT infrastructure. This application was created in May of 2019.

## Justification of Artifact Three:

* I chose this artifact because it shows a real-world use of a database to provide core functionality to a web application. In web development and design, you generally use some type of language specific driver to interact with a database instead of directly modifying the database itself. This artifact showcases the use of an object-relational mapping tool called SQLAlchemy to convert code written in the Python language to data objects that can be inserted into a PostgreSQL database and modified via the SQLAlchemy driver psycopg2. This artifact contains four files that make up the core of the web application functionality. The files that comprise the bulk of the database functionality are models.py which creates the Python object that represents a table entry in the PostgreSQL database, and routes.py which uses SQLAlchemy to perform CRUD operations. A typical directory structure for a Flask module contains the following:
* I. __init__.py – This file is defined as a “Blueprint” and allows this module to be called by the application upon initialization. This is a design typical in a Flask application. 
* II. forms.py – This Python file is the interface to the database. This is the form that users would POST to the database to Create and Update new and existing computer and network devices present in their home or office
* III. models.py – This is the Python file that creates a Class object that represents a table entry in the PostgreSQL database. This uses the concept of Object-relational mapping to allow programmatic interaction between the SQL database language and the Python language. In addition to creating tables in the database this concept of Class based models allows, through Flask, relationships between other models that allows the modification of other tables through the relationship established within this model. 
* IV. routes.py – This is the file that sets up the routing between the various web pages and their respective functionality. The routes.py model lies at the heart of RESTful architecture and brings the application to the users via the web. Within routes.py, SQLAlchemy is used extensively to perform the typical Create, Read, Update, Delete (CRUD) operations typical of a RESTful web application.


## Reflection on Artifact Three:

* I was a bit disappointed that I was not able to convert the database to MongoDB, but in the process, I was able to get a good refresher on using MongoDB, PostgreSQL, Flask, and SQLAlchemy. It is always difficult for me to revisit old code that has not been touched in a while. It is funny how something you originally spent so much time and effort on, where at one point you knew it like the back of your hand, can become so foreign and confusing because it has been stable for so long there hasn’t been a need to revisit it. After some considerable effort of going through the program, understanding comes back relatively quickly and in a way you time travel back to a place when developing the application was a new and experience. 