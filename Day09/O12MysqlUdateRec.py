
import pymysql

conn = pymysql.connect(host="localhost", database="employee", user="root", password="", port=3306)

cur = conn.cursor()

query = "update employee set dept = 'Boxing' where empid = 'emp001'"

cur.execute(query)

conn.commit()

conn.close()

