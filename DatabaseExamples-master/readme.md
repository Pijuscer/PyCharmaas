
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