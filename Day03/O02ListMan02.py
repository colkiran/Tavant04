"""
sort and sorted
----------------
sort will sort the original list
sorted will sort the list and returns a copy of it

"""


print('sort'.center(40, "-"))
l = [10, 5, 8, 1, 9, 4, 2, 6, 3, 7]
print(f"l :{l}")

res1 = sorted(l)
print(f"res1 :{res1}")
res2 = sorted(l, reverse=True)
print(f"res2 :{res2}")

print("-" * 40)
l = [10, 'zebra', 'x ray', 5, 'apple', 'blue', 8, 'yellow', 'white', 1, 'green', 'orange', 9,
     'violet', 'red', 4, 'cat', 'dog', 2, 'pink', 'mango', 6, 3, 7, 19, 145, 1234, 10032, 28,
     2045, 231, 36, 310, 3021]

print(f"l :{l}")

print("-" * 40)
res = sorted(l, key=ascii)
print(f"res :{res}")

print("-" * 40)
cities = ['thiruvanathapuram', 'hyderabad', 'bangalore', 'ooty', 'mumbai', 'chennai', 'vishakapatnam',
          'delhi', 'kanyakumari', 'mysore', 'kolar']
print(f"cities :{cities}")

print("-" * 40)
res = sorted(cities, key=len)
print(f"res :{res}")

print("-" * 40)
months = ['apr', 'aug', 'dec', 'feb', 'mar', 'may', 'nov', 'oct', 'jan', 'jun', 'jul', 'sep']
print(f"months :{months}")

print("-" * 40)
from calendar import month_name
# print(list(month_name))

def sortMonths(mon):
    lst = []
    for mnt in list(month_name):
        lst.append(mnt[0:3].lower())
    if mon in lst:
        return lst.index(mon)

res = sorted(months, key=sortMonths)
print(f"res :{res}")

print("=" * 40)

from datetime import datetime
mon=['apr','aug','dec','feb','mar','may','nov','oct','sep','jan','jun','jul']
print(f"before sorting:{mon}")
mon.sort(key=lambda date: datetime.strptime(date, '%b'))
print(f"after sorting:{mon}")

print("reversed".center(40, "-"))

l = [10, 5, 8, 1, 9, 4, 2, 6, 3, 7]
print(f"l :{l}")

res = list(reversed(l))
print(f"res :{res}")

print("{x:-^40}".format(x = "clear"))
l = [10, 5, 8, 1, 9, 4, 2, 6, 3, 7]
print(f"l :{l}")

l.clear()
print(f"l :{l}")
