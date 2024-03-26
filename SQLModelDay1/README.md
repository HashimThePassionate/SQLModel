# SQLModelDay1: A Step-by-Step Guide

This project demonstrates how to use SQLModel, a Python library for creating database models and interacting with relational databases. It provides a structured approach to database interaction, simplifying data access and manipulation in your applications.

## Project Structure:
The project is organized into several well-defined modules for better maintainability:
-   main.py:
    The entry point of the application. It handles database creation, table creation, and calls the function to insert sample customer data.
-   connection_string.py:
    Stores the database connection string securely, separating connection details from the main code.
-   models.py:
    Defines the Customer model that represents the structure of your customer data in the database.
-   engines.py: 
    stablishes the connection to the database engine using the connection string from connection_string.py.
-   create_records.py: 
    Creates sample customer objects and inserts them into the database using a session.

##  Prerequisites:
* Python 3.8 or later
* pipx
* SQLModel library 
* psycopg2
* psycopg-binary
* serverless neon database string

##  Installation:
- Download python from https://www.python.org/
- python -m pip install --user pipx
- python -m pipx ensurepath
- pipx install poetry
- poetry --version
- poetry new sqlmodelday1
- cd sqlmodelday1
- Open pyproject.toml file 

and paste this

```python
python = "^3.12"
sqlmodel = "^0.0.16"
psycopg = {extras = ["binary"], version = "^3.1.18"}
psycopg2 = "^2.9.9"
```
- poetry install

### Now Follow all main directory structure
