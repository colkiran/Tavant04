
import sqlite3
from prettytable import from_db_cursor

conn = sqlite3.connect(database="employee.sqlite3")

cur = conn.cursor()

query = "select * from employee"

cur.execute(query)

pt = from_db_cursor(cur)

# for row in cur.fetchall():
#     print(row)

pt.align['empname'] = "l"
pt.align['desig'] = "l"
pt.align['dept'] = "l"
pt.align["salary"] = "r"

conn.close()

print(pt)