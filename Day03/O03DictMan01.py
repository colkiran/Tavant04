
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'sachin'), ('runs', 145), ('oppon', 'ENG'), ('venue', 'lords')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name="Rahul", runs=89, oppon="NZL", venue="Auckland")
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
player = {'name': 'Sachin', 'runs': 98, 'oppon': "AUS", 'venue': 'perth'}
print(f"player :{player}")

# read the contents
print(f"Name :{player['name']}")
print(f"Venue :{player['venue']}")

for i in player:
    print(i, "=>", player[i],  end=" ")
print()

# update
print("-" * 40)
print(f"player :{player}")
player['runs'] = 120
player['year'] = '1998'
player['age'] = 28
print(f"player :{player}")

# delete
print("-" * 40)
print(f"player :{player}")
del player['age']
print(f"player :{player}")

print("-" * 40)
print(f"Name :{player['name']}")
# print(f"Name :{player['age']}")

print(f"Age :{player.get('age')}")
print(f"Age :{player.get('age', 'please enter a valid key...')}")

print("-" * 40)
print(dir(player))