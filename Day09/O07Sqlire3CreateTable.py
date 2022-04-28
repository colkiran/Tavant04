

import sqlite3

conn = sqlite3.connect(database="employee.sqlite3")

cur = conn.cursor()

query = """
create table employee (
empid varchar(6) primary key,
empname varchar(50) not null,
desig varchar(50) not null,
dept varchar(50) not null,
salary real not null
)
"""

cur.execute(query)

conn.close()
