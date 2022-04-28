
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", port=3306)

cur = conn.cursor()

query = "create database employee"

cur.execute(query)

conn.close()
