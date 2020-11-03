
1: Sukurti 2 lenteles(Tables) viena turi būti "Customers" kita "Companies"

2: Customers table turi turėti FOREIGN KEY (Paaiškinimas kas yra Foreign key: https://code.tutsplus.com/articles/sql-for-beginners-part-3-database-relationships--net-8561)

3: Sukurti CRUD abiem lentelėm(Tables).

4: Parašyti JOIN funkcija. pvz: 

def join_customers_companies:
    query = "SQL query kuriame naudosite JOIN"
    with DatabaseContextManager("relationships") as db:
        db.execute(query)
        for row in db.fetchall()
            print(row)
 from database import DatabaseContextManager
import sqlite3

# with DatabaseContextManager("relationships") as db:
#     db.execute(query, parameters)

# "Foreign key table"
# Table = "Customers"
# Fields = [customer_id,first_name, last_name, age, Foreign Key (compnay_id) References Companies(company_id)]

# Table = "Companies"
# Fields = [company_id,company_name, employee_count]

# JOIN OUTPUT: 1,John,johnathan, 30, 2 , 2 , Google, 500


    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()

def create_table_customers():
    query = """CREATE TABLE IF NOT EXISTS Customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first name TEXT,
    last_name TEXT,
    age INTEGER,
    customer_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES Companies(company_id))"""
    with DatabaseContextManager("db") as db:
        db.execute(query)

def create_table_companies():
    query = """CREATE TABLE IF NOT EXISTS Companies(
    company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    employee_count TEXT)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)

# ------------------------Customer CRUD------------------------
# CRUD stands for Create, Read, Update, Delete
# Create or in SQL INSERT is used to create new records in the database.
# Read(get) or in SQL SELECT is used to read data from the database
# Update is used to update data for already existing record
# Delete for deleting records that are already created.

# Create function Customer
def create_customers(first_name: str, last_name: str, age: int):
    query = """INSERT INTO Customers(first_name, last_name, age) VALUES(?,?,?,?)"""
    # Question marks are used in initial query to have placeholders for upcoming parameters.
    # (This is used to protect ourselves from SQL Injection attacks)
    #  Instead of question marks in some languages/sql engines we use %, s%
    parameters = [first_name, last_name, age]
    # Parameters are used to pass values that were given when calling the function.
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)
        # We can pass sql and parameters to execute method which will set our values by order from parameters array or touple

# Read function Customer
def get_customers(first_name):
    query = """SELECT * FROM Customer
               WHERE first_name = ?"""
    parameters = [first_name]
    with DatabaseContextManager("db") as cursor:
        cursor.execute(query, parameters)
        for record in cursor.fetchall():
            print(record)
    print("------------------------------------------------------")
    # print for convenience in terminal

# Update function Customer
def update_customers_first_name(old_first_name: str, new_first_name: str):
    query = """UPDATE Customers
                SET first_name = ?, 
                WHERE first_name = ?"""
    parameters = [new_first_name, old_first_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)

# Delete function Customer
def delete_customers(first_name: str):
    query = """DELETE FROM Customers
                WHERE first_name = ?"""
    parameters = [first_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)

# ------------------------Companies CRUD------------------------
def create_companies(company_name: str, employee_count: str):
    query = """INSERT INTO Companies(company_name, employee_name) VALUES(?, ?)"""
    parameters = [company_name, employee_count]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)

def get_companies():
    query = """SELECT * FROM Companies"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)

def update_companies_name(old_employee_name: str, new_employee_name: str):
    query = """UPDATE Companies
                SET employee_name = ?
                WHERE employee_name = ?"""
    parameters = [new_employee_name, old_employee_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_companies(employee_name: str):
    query = """DELETE FROM Companies
                WHERE employee_name = ?"""
    parameters = [employee_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_customers_companies():
    query = """SELECT * FROM Customers
                JOIN Companies
                    ON Customers.company_id = Customers.company_id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for row in db.fetchall():
            print(row)