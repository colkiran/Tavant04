
import pymysql

conn = pymysql.connect(host="localhost", database="employee", user="root", password="", port=3306)

cur = conn.cursor()

# query = "insert into employee values ('EMP001', 'Mike Tyson', 'MGR', 'Sports', 85000.00)"
# query = "insert into employee values ('EMP002', 'Sacin Tendulkar', 'CEO', 'Cricket', 135000.00)"
# query = "insert into employee values ('EMP003', 'Lione Messi', 'Director', 'Football', 150000.00)"
# query = "insert into employee values ('EMP004', 'Roger Fedrrer', 'PM', 'Tennis', 120000.00)"
query = "insert into employee values ('EMP010', 'Mike', 'PL', 'Badmiton', 90000.00)"

cur.execute(query)

conn.commit()

conn.close()
