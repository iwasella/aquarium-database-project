# aquarium-database-project
This is a Python-based Command Line Interface (CLI) application designed to manage a restaurant database. The project uses SQLite, a lightweight, serverless, embedded database, accessed via Python's built-in sqlite3 library.

Setup and Installation
1. Create and Activate Virtual Environment (Recommended)
It is recommended to work from a python venv (virtual environment). Follow these instructions to set up & activate your venv: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

Python comes with the sqlite3 library. SQLite is a lightweight, embedded database and does not need to be run from a separate process.


This tutorial introduces you to how to use the sqlite3 library to interface with a SQLite db: https://docs.python.org/3/library/sqlite3.html

A test file (test.py) has already been provided to verify and show sqlite3 functionality. Running the file should display the following output:
```
('Monty Python and the Holy Grail', 1975, 8.2)
('And Now for Something Completely Different', 1971, 7.5) 
```
SQLite is an embedded database — meaning:
- there is no database server to install
- your entire database lives inside a single file (e.g., aquarium.db)
- Python includes SQLite support through the built-in sqlite3 module


2. Run the Installer (Initialize Database)
python3 run_first.py

Running Test Queries
python3 run_test_queries.py  

**NOTE** Recommended to run test queries first before using the CLI.  
After running test queries :  
Remove restaurant.db, generate it back, and then go forward to the CLI (better to start CLI with a clean slate).  

To interact with the main CLI application:
python3 main.py

All database operations are located in crud.py.

If something breaks or you want a clean slate:
rm restaurant.db
python3 run_first.py


Technologies Used
Python (CLI interface, SQLite operations)
SQLite3 (lightweight database)
SQL (schema, seed data, queries




