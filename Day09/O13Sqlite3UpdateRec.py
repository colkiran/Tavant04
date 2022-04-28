
import sqlite3

conn = sqlite3.connect(database="employee.sqlite3")

cur = conn.cursor()

query = "update employee set dept = 'Boxing' where empid = 'EMP001'"

cur.execute(query)

conn.commit()

conn.close()

