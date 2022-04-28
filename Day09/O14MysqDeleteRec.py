
import pymysql

conn = pymysql.connect(host="localhost", database="employee", user="root", password="", port=3306)

cur = conn.cursor()

query = "delete from employee where empid = 'EMP010'"

cur.execute(query)

conn.commit()

conn.close()

