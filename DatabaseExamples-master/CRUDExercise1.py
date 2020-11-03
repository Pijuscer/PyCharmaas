from database import DatabaseContextManager


# Tables = "Customer"
# fields = [first_name, last_name, address, age]

def create_table_customer():
    query = """CREATE TABLE IF NOT EXISTS Customer(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    address TEXT,
    age INTEGER)"""
    with DatabaseContextManager("CRUD") as db:
        db.execute(query)


# Create function
def create_customer(first_name: str, last_name: str, addres: str, age: int):
    query = """INSERT INTO Customer(first_name, last_name, address, age) VALUES(?,?,?,?)"""

    parameters = [first_name, last_name, addres, age]
    with DatabaseContextManager("CRUD") as db:
        db.execute(query, parameters)


# Read function
def get_customer():
    query = """SELECT * FROM Customer"""

    with DatabaseContextManager("CRUD") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


# print for convenience in terminal


# Update function
def update_customer(first_name, last_name, age):
    query = """UPDATE Customer
                SET age = ?
                WHERE first_name = ? AND last_name = ?"""

    parameters = [age, first_name, last_name]
    with DatabaseContextManager("CRUD") as db:
        db.execute(query, parameters)


# Delete function
def delete_customer(last_name):
    query = """DELETE FROM Customer
                WHERE last_name = ?"""
    parameters = [last_name]
    with DatabaseContextManager("CRUD") as db:
        db.execute(query, parameters)


# create_table_customer() # paleisti tik viena karta
create_customer("Jonas", "Jonaitis", "Kaunas", 30)
update_customer("Jonas", "Jonaitis", 20)
get_customer()
