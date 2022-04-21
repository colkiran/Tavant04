
# lambdas

def addMe(x, y):
    return x + y

a = addMe
res = a(20, 30)
print(f"res :{res}")

print("-" * 40)

b = lambda x, y: x + y
res = b(10, 20)

print(f"res :{res}")

# lambdas are best used with = map, filter and reduce (functools)
# map - execute the expression on a given list
l = list(range(1, 11))
print(f"l :{l}")

res = list(map(lambda x: x ** 2, l))
print(f'res :{res}')

# expenses in dollars - converted into rupees
expenses = [50, 250, 800, 1200, 450, 2400, 7500]

exp_rs = list(map(lambda x: x * 76.1, expenses))
print(f"exp_rs :{exp_rs}")

print("-" * 40)
months = ['apr', 'aug', 'dec', 'feb', 'mar', 'may', 'nov', 'oct', 'jan', 'jun', 'jul', 'sep']
print(f"months :{months}")

print("-" * 40)
from calendar import month_name
srtMon = sorted(months, key=list(map(lambda mn: mn[0:3].lower(), list(month_name))).index)
print(f"Sorted Months :{srtMon}")

from datetime import datetime
res = sorted(months, key=lambda date: datetime.strptime(date, '%b'))
print(f"res :{res}")

print("=" * 40)
# filter = expression in lambda should return true or false
l1 = list(range(1, 26))
print(f"l1 :{l1}")

res = list(filter(lambda x: x % 3 == 0, l1))
print(f"res :{res}")

print("=" * 40)
# reduce - functools
from functools import reduce
l = [10, 6, 3, 8, 15, 7, 9, 11, 13, 5]
print(f"l :{l}")

larNum = reduce(lambda x, y: x if x > y else y, l)
print(f"Largest Num :{larNum}")

sumNum = reduce(lambda x, y: x + y, l)
print(f"Sum of numbers :{sumNum}")

"""
lambda syntax will be used in comprehension
comprehension - iterate through a collection (list, dictionary) using lambda syntax 
"""