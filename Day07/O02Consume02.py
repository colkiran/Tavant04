
import mypackage.mymodule as m
from mypackage.mymodule import Employee

m.greet("MS Dhoni")

print("-" * 40)
emp1 = Employee("Steve", 38)
emp1.get_details()

print("-" * 40)

res = m.sum(10, 20)
print(f"res :{res}")

emp1 = Employee("Jack", 35)
emp1.get_details()

