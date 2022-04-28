
import pymysql

conn = pymysql.connect(host="localhost", database="employee", user="root", password="", port=3306)

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
