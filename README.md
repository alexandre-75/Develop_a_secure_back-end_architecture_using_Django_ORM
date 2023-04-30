<p align="center"><img src="pictures\16007804386673_P10.png" alt="logo" /></p>

## 1 . The Project

- Use the **Django** framework.
- Use the **Django REST framework** for the API
- Using server-side rendering in **Django**.
- Using **JSON Web Tokens (JWT)** to secure the API
- construct an **entity-relationship diagram (ERD)**
- Use **Jazzmin**

## 2 . Context
- Epic Events meets the needs of start-ups wanting to organize “epic parties”.
- Epic Events is a consulting and event management company.
- My job is to manage the company's outdated customer relationship management (CRM) software.

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


#### 6 . 1 - CRM Users  -  CRM Events

<p align="center"><img src="https://github.com/alexandre-75/Develop_a_secure_back-end_architecture_using_Django_ORM/blob/main/pictures/Capture%20d%E2%80%99%C3%A9cran%202023-04-30%20144805.jpg?raw=true" alt="" /></p>

###### Events
- Sales group = [GET] events (attribution) + [POST] events
- Support group = [GET] [PUT] events (attribution)
- Management group = [GET] [PUT] [DELETE] all events + [POST] events

###### Users
- Management group = [GET] [PUT] [DELETE] all users + [POST] users

#### 6 . 2 - CRM Clients  -  CRM Contratcs
<p align="center"><img src="https://github.com/alexandre-75/Develop_a_secure_back-end_architecture_using_Django_ORM/blob/main/pictures/Capture%20d%E2%80%99%C3%A9cran%202023-04-30%20144742.jpg?raw=true" alt="" /></p>

###### clients / contracts :

- Sales group = [GET] [PUT] clients (attribution) + [POST] clients
- Support group = [GET] clients (attribution)
- Management group = [GET] [PUT] [DELETE] all clients + [POST] clients

##  7 . Project download

_Tested on Windows 10, Python 3.10.6. / Django 4.2. / djangorestframework 3.14.0_


- [Technical Specifications ( french )](https://github.com/alexandre-75/Develop_a_secure_back-end_architecture_using_Django_ORM/blob/main/pictures/PDF/CRM%2B-%2BExigences%2Btechniques.pdf)

- [Fonctional Specifications ( french )](https://github.com/alexandre-75/Develop_a_secure_back-end_architecture_using_Django_ORM/blob/main/pictures/PDF/CRM%2B-%2BExigences%2Bfonctionnelles.pdf)


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
- ***Run the server*** by executing the command :
  ```
  python manage.py runserver
  ```

- Open your favorite browser and navigate to the ***local development server*** at :
  ```
  http://127.0.0.1:8000/
  ```