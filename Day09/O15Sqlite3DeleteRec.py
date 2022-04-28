

import sqlite3

conn = sqlite3.connect(database="employee.sqlite3")

cur = conn.cursor()

query = "delete from employee where empid = 'EMP010'"

cur.execute(query)

conn.commit()

conn.close()

