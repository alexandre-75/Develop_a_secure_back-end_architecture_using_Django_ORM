<p align="center"><img src="pictures\16007804386673_P10.png" alt="logo" /></p>

## Summary :

- [1 - The Project](#1--the-project)
- [2 - The Context](#2--context)
- [3 - The Database](#3--database)
- [4 - API Documentation](#4--api-documentation)
- [5 - Entity-Relationship Diagram (ERD)](#5--entity-relationship-diagram-erd)
- [6 - Permissions](#6--permissions)
    - [6 . 1 - CRM Users - CRM Events](#6--1---crm-users---crm-events)
    - [6 . 2 - CRM Clients - CRM Contratcs](#6--2---crm-clients---crm-contratcs)
- [7 . Project download](#7--project-download)
    - [7 . 1 - project recovery](#7--1---project-recovery)
    - [7 . 2 - Creating a virtual environment](#7--2---creating-a-virtual-environment)
    - [7 . 3 - Installing packages](#7--3---installing-packages)
    - [7 . 4 - Start the program](#7--4---start-the-program)
    - [7 . 5 - create a superuser](#7--5---create-a-superuser)
- [8 . Django admin site front-end interface](#8--django-admin-site-front-end-interface)


## 1 . The Project

- Use the **Django** framework.
- Use the **Django REST framework** for the API
- Using server-side rendering in **Django**.
- Using **JSON Web Tokens (JWT)** to secure the API
- Construct an **entity-relationship diagram (ERD)**
- Using **PostgreSQL** as a database
- Use **Jazzmin**

## 2 . Context
- Epic Events meets the needs of start-ups wanting to organize “epic parties”.
- Epic Events is a consulting and event management company.
- The vendor who is responsible for the CRM has been hacked.
- A CRM (Customer Relationship Management) is a system used by companies to manage their interactions with current and potential customers.
- Consequence : develop a secure CRM system internal to the company.
    - **creating a user interface with permissions.**
    - **creation of an API with permissions.**

## 3 . Database

- PostgreSQL is a free, open-source relational database management system (RDBMS).
- PostgreSQL is used to store and manage data.
- PostgreSQL is a relational and secure database.

- Create a database in Postgresql, and replace in settitngs.py the configuration with your database.
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<name-bdd>',
        'USER': '<name_of_the_admin_user_of_your_db>',
        'PASSWORD': '<password_of_your_admin_user>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
## 4 . API Documentation

Detailed API documentation is available at:

[API Documentation](https://documenter.getpostman.com/view/24753025/2s93eSZFJw)

You will find in this documentation all the detailed API endpoints

## 5 . Entity-Relationship Diagram (ERD)

- It graphically represents the structure of a database
- An ERD makes it easier to understand the data
<p align="center"><img src="https://github.com/alexandre-75/Develop_a_secure_back-end_architecture_using_Django_ORM/blob/main/pictures/Capture%20d%E2%80%99%C3%A9cran%202023-04-30%20144637.jpg?raw=true" alt="ERD" /></p>

## 6 . Permissions
- CRM users are divided into three categories: Management, Sales, Support.
- user has **access to the data**, depending on the group (Management, Support, Sales)
- user has **access to HTTP requests**, depending on the group (Management, Support, Sales)
- Using JSON Web Tokens (JWT) to secure the API


#### 6 . 1 - CRM Users - CRM Events

<p align="center"><img src="https://github.com/alexandre-75/Develop_a_secure_back-end_architecture_using_Django_ORM/blob/main/pictures/Capture%20d%E2%80%99%C3%A9cran%202023-04-30%20144805.jpg?raw=true" alt="" /></p>

###### Events
- Sales group = [GET] events (attribution) + [POST] events
- Support group = [GET] [PUT] events (attribution)
- Management group = [GET] [PUT] [DELETE] all events + [POST] events

###### Users
- Management group = [GET] [PUT] [DELETE] all users + [POST] users

#### 6 . 2 - CRM Clients - CRM Contratcs
<p align="center"><img src="https://github.com/alexandre-75/Develop_a_secure_back-end_architecture_using_Django_ORM/blob/main/pictures/Capture%20d%E2%80%99%C3%A9cran%202023-04-30%20144742.jpg?raw=true" alt="" /></p>

###### clients / contracts :

- Sales group = [GET] [PUT] clients (attribution) + [POST] clients
- Support group = [GET] clients (attribution)
- Management group = [GET] [PUT] [DELETE] all clients + [POST] clients

##  7 . Project download

_Tested on Windows 10, Python 3.10.6. / Django 4.2. / djangorestframework 3.14.0_


- [Technical Specifications ( french )](https://github.com/alexandre-75/Develop_a_secure_back-end_architecture_using_Django_ORM/blob/main/pictures/PDF/CRM%2B-%2BExigences%2Btechniques.pdf)

- [Fonctional Specifications ( french )](https://github.com/alexandre-75/Develop_a_secure_back-end_architecture_using_Django_ORM/blob/main/pictures/PDF/CRM%2B-%2BExigences%2Bfonctionnelles.pdf)

- [Technical Requirements ( french )](https://openclassrooms.notion.site/5a4642c14eef48c78c9e1b98a8e0a3fc?v=12d25b7081ba436a9e06f0e99cdcae25)


####  7 . 1 - project recovery

    $ git clone https://github.com/alexandre-75/Develop_a_secure_back-end_architecture_using_Django_ORM.git

####  7 . 2 - Creating a virtual environment

    python<version> -m venv nom_env_virtuel

    Activate the environment  `mon_env_virtuel\Scripts\activate` (Windows)

####  7 . 3 - Installing packages

    pip<version> install -r requirements.txt
    
####  7 . 4 - Start the program

- From the project root folder, go with the terminal to the ***source*** folder :
    ```
     cd source/
     ```
 - migrations for database initialization:
    ```
    python manage.py makemigrations
    ```
    Then:
    ```bash 
    python manage.py migrate
    ```  
     
- ***Run the server*** by executing the command :
  ```
  python manage.py runserver
  ```

- Open your favorite browser and navigate to the ***local development server*** at :
  ```
  http://127.0.0.1:8000/
  ```
  
#### 7 . 5 - create a superuser
  - create your own content and for this, you need to create a superuser with :
    ```
    python manage.py createsuperuser
    ```
   
## 8 . Django admin site front-end interface
  
  - Jazzmin is a Python package that provides a custom admin interface for Django
  - It replaces the default Django admin interface
  - It is available as an open source package
  - [Jazzmin official documentation](https://django-jazzmin.readthedocs.io/)
  
  <p align="center"><img src="https://github.com/alexandre-75/Develop_a_secure_back-end_architecture_using_Django_ORM/blob/main/pictures/ezgif.com-video-to-gif%20(2).gif?raw=true" alt="admin" /></p>