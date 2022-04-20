
"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
'pop', 'popitem', 'setdefault', 'update', 'values'
"""
player = {'name': 'Rahul', 'age': 36, 'runs': 135, 'oppon': 'sri lanka', 'venue': 'chepauk', 'year': 2003}
print(f"player :{player}")

ky = player.keys()
print(f"ky :{ky}")
print("-" * 40)

for k in player.keys():
    print(k + "=>" + str(player[k]))

print("values".center(40, "-"))
player = {'name': 'Rahul', 'age': 36, 'runs': 135, 'oppon': 'sri lanka', 'venue': 'chepauk', 'year': 2003}
print(f"player :{player}")

vl = player.values()
print(f"values :{vl}")

print("setdefault".center(40, "-"))
player = {'name': 'Rahul', 'age': 36, 'runs': 135, 'oppon': 'sri lanka', 'venue': 'chepauk'}
print(f"player :{player}")

player.setdefault('runs', 150)
player.setdefault('year', 2003)
player.setdefault('age', 32)
print(f"player :{player}")

print("fromkeys".center(40, "-"))
cities = ['blr', 'che', 'hyd', 'mum', 'del', 'kol']
print(f"cities :{cities}")
res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")
res2 = dict.fromkeys(cities, 23)
print(f"res2 :{res2}")

print("{y:-^40}".format(y="pop"))
player = {'name': 'Rahul', 'age': 36, 'runs': 135, 'oppon': 'sri lanka', 'venue': 'chepauk', 'year': 2003}
print(f"player :{player}")

res = player.pop('age')
print(f"res :{res}")
print(f"player :{player}")

res1 = player.pop("year")
print(f"res1 :{res1}")
print(f"player :{player}")

print("popitem".center(40, "-"))
player = {'name': 'Rahul', 'age': 36, 'runs': 135, 'oppon': 'sri lanka', 'venue': 'chepauk', 'year': 2003}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")
print(f"player :{player}")

res1 = player.popitem()
print(f"res1 :{res1}")
print(f"player :{player}")
