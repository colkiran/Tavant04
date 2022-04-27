import sys

inv = 1
num = 0

try:
    inv = 1 / nm

except ZeroDivisionError as z:
    print("Exception raised....")
    print(z)
except ValueError as v:
    print("Exception raised....")
    print(v)
except TypeError as t:
    print("Exception raised.....")
    print(t)
except Exception as e:
    print("Exception1 raised.....")
    print(e)
else:
    print(f"inv :{inv}")
finally:
    print("completed the process of division......")
