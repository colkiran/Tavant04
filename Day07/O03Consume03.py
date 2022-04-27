
"""
all modules should be placed in any place where sys.path is pointing to

"""
import sys

sys.path.append("C:\\Delhi")

for pth in sys.path:
    print(pth)

import gurgaon.mymodule as m
from gurgaon.mymodule import Employee

m.greet(m.gstName)
m.greet("Brain Lara")

print("-" * 40)
emp1 = Employee("Micheal", 34)
emp1.get_details()
