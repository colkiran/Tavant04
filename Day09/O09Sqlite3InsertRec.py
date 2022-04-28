


import sqlite3

conn = sqlite3.connect(database="employee.sqlite3")

cur = conn.cursor()

query = "insert into employee values ('EMP010', 'Mike', 'MGR', 'Sports', 85000.00)"
# query = "insert into employee values ('EMP002', 'Sacin Tendulkar', 'CEO', 'Cricket', 135000.00)"
# query = "insert into employee values ('EMP003', 'Lione Messi', 'Director', 'Football', 150000.00)"
# query = "insert into employee values ('EMP004', 'Roger Fedrrer', 'PM', 'Tennis', 120000.00)"
# query = "insert into employee values ('EMP005', 'PV Sindhu', 'PL', 'Badmiton', 90000.00)"

cur.execute(query)

conn.commit()

conn.close()
