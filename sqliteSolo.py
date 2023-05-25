import sqlite3
from Employee import Employee

conn = sqlite3.connect()
c = conn.cursor()

c.execute("""CREATE TABLE education (
            MiddleSchool TEXT,
            HighSchool TEXT,
            University TEXT,
            DegreeClass REAL
            )""")


def insert_employee(emp):
    with conn: #context manager -> same as with open file
        c.execute("INSERT INTO education VALUES(:first, :second, :pay)", {'first': emp.first,
                                                                          'second': emp.last,
                                                                          'pay': emp.pay
                                                                          })

def get_employees_by_Middleschool(school):
    c.execute("SELECT * FROM education WHERE MiddleSchool = :school", {'school': school})
    return c.fetchall()

def update_degree(emp, degree):
    with conn:
        c.execute("UPDATE education SET DegreeClass = :degree"
                  "WHERE ")

def remove_employee(emp):
    pass
