import sys

inv = 1
num = 0

try:
    inv = 1 / num

except :
    print("Exception raised....")
    print(sys.exc_info()[0])                # exception keyword
    print(sys.exc_info()[1])                # exception string
else:
    print(f"inv :{inv}")
finally:
    print("completed the process of division......")
