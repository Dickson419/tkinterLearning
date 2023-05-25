"""
BASIC OVERVIEW - Key commands
Add, update, delete and get information of employees from the database
"""
import sqlite3

conn = sqlite3.connect("employee.db") #possible to do in memory database with ':memory:'
c = conn.cursor() #cursor

#make the table and columns --> error if run once made once so commented out
# c.execute("""CREATE TABLE employees (
#             FirstName TEXT,
#             LastName TEXT,
#             Pay REAL
#             )""")

#add to the database
#c.execute("INSERT INTO employees VALUES ('Steven', 'Dickson', 34500.25)")
c.execute(("INSERT INTO employees VALUES ('Mookie', 'Dickson', 70000.00) "))
conn.commit()

#query the database - SELECT
c.execute("SELECT * FROM employees WHERE LastName ='Dickson'")
print(c.fetchone()) #returns one result
print(c.fetchall()) #-> returns a list i.e same firstname, lastname etc


conn.commit() #add changes
conn.close()