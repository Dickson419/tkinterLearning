import sqlite3
from Employee import Employee

conn = sqlite3.connect('employee.db')
c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#             FirstName TEXT,
#             LastName TEXT,
#             Pay REAL
#             )""")

def insert_employee(emp):
    with conn: #context manager -> same as with open file
        c.execute("INSERT INTO employees VALUES(:first, :second, :pay)", {'first': emp.first,
                                                                          'second': emp.last,
                                                                          'pay': emp.pay
                                                                          })

def get_employee_by_lastname(lastname):
    c.execute("SELECT * FROM employees WHERE LastName = :last", {'last':lastname})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET Pay = :pay
                  WHERE FirstName = :first AND LastName = :last""", {'first':emp.first, 'last': emp.last, 'pay':pay})

def remove_employee(emp):
    with conn:
        c.execute("""DELETE FROM employees WHERE FirstName = :first AND LastName = :last""", {'first': emp.first, 'last':emp.last})


#add variables, objects, to the database
emp1 = Employee("Andrea", "Moon", 45000)
emp2 = Employee("Carol", "Moon", 100000)

insert_employee(emp1)
insert_employee(emp2)

all_employees = get_employee_by_lastname('Moon')
print(all_employees)

pay = update_pay(emp2, 120000)
remove_employee(emp1)
all_employees = get_employee_by_lastname('Moon')

print(all_employees)

conn.close()