
"""
class attributes are static variables and they hold same data across objects

"""

class Player:
    team = "India"

    def __init__(self, name, age):                  # constructor
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name :{self.name}\nAge :{self.age}")

ply1 = Player("Sachin", 38)
ply2 = Player("Rahul", 35)

ply1.get_details()
print("-" * 40)

ply2.get_details()
print("-" * 40)

print(Player.team)
print(ply1.team)
print(ply2.team)

print("-" * 40)
Player.team = "MI"
print(Player.team)
print(ply1.team)
print(ply2.team)

print("-" * 40)
ply2.team = "RCB"
print(ply2.team)
print(Player.team)
print(ply1.team)

print("-" * 40)
print(ply2.team)
print(ply2.__dict__)

print(ply1.__dict__)

print("-" * 40)
print(Player.__dict__)

