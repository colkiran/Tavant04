
import csv

with open("Employee.csv", "r") as CSVR:
    emp_details = csv.reader(CSVR)
    colname = next(emp_details)
    print(colname)

    for rec in emp_details:
        print(*rec)

CSVR.close()

