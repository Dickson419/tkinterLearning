"""
BASIC OVERVIEW - Key commands with variables
Add, update, delete and get information of employees from the database
"""
import sqlite3
from Employee import Employee


#conn = sqlite3.connect("employee.db") #possible to do in memory database with ':memory:'
conn = sqlite3.connect('employee.db') #keeps table in RAM. Good for testing
c = conn.cursor() #cursor

#add variables, objects, to the database
emp1 = Employee("Andrea", "Moon", 45000)
emp2 = Employee("Carol", "Moon", 100000)
print(emp1.first)
print(emp2.first)

#Enter data - string formatiing/place holders vulnerable to sql injection attacks
#c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp1.first, emp1.last, emp2.pay)) #second argument -> tuple of values
#Or alternatively...

c.execute("INSERT INTO employees VALUES(:first, :second, :pay)", {'first':emp2.first,
                                                                  'second':emp2.last,
                                                                  'pay': emp2.pay
                                                                  }) #placeholders matched to a dictionary

c.execute("INSERT INTO employees VALUES(:first, :second, :pay)", {'first':emp1.first,
                                                                  'second':emp1.last,
                                                                  'pay': emp1.pay
                                                                  }) #placeholders matched to a dictionary

c.execute("SELECT * FROM employees WHERE LastName = :second", {'second':'Moon'}) #dict as placeholder matches to :second

print(c.fetchall())


conn.commit() #add changes
conn.close()