<p align="center"><img src="pictures\16007804386673_P10.png" alt="logo" /></p>

## The Project

- Use the **Django** framework.
- Use the **Django REST framework** for the API
- Using server-side rendering in **Django**.
- Using **JSON Web Tokens (JWT)** to secure the API
- construct an **entity-relationship diagram (ERD)**

## Context
- Epic Events meets the needs of start-ups wanting to organize “epic parties”.
- Epic Events is a consulting and event management company.
- My job is to manage the company's outdated customer relationship management (CRM) software.

## Database

- PostgreSQL is a free, open-source relational database management system (RDBMS).
- PostgreSQL is used to store and manage data.
- PostgreSQL est une base de données relationnelle, performante, évolutive, multi-plateforme et sécurisée.

##  Project download

_Tested on Windows 10, Python 3.10.6. / Django 4.2. / djangorestframework 3.14.0_


- [Technical Specifications ( french )](https://github.com/alexandre-75/Develop_a_secure_back-end_architecture_using_Django_ORM/blob/main/pictures/PDF/CRM%2B-%2BExigences%2Btechniques.pdf)

- [Fonctional Specifications ( french )](https://github.com/alexandre-75/Develop_a_secure_back-end_architecture_using_Django_ORM/blob/main/pictures/PDF/CRM%2B-%2BExigences%2Bfonctionnelles.pdf)

####  1. project recovery

    $ git clone https://github.com/alexandre-75/Develop_a_secure_back-end_architecture_using_Django_ORM.git

####  2. Creating a virtual environment

    python<version> -m venv nom_env_virtuel

    Activate the environment  `mon_env_virtuel\Scripts\activate` (Windows)

####  3. Installing packages

    pip<version> install -r requirements.txt
    
####  4. Start the program

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