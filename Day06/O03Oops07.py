
"""
operator overloading => + => adding, concatenation

Magic Methods   =>   __add__()    => double underscore => dunder add
3 + 4
"""

# magic methods
class Player:
    team = "India"

    def __init__(self, name, age):                  # constructor
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name :{self.name}\nAge :{self.age}"

ply1 = Player("Sachin", 49)
print(str(ply1))
print("-" * 40)

print(ply1)                     # implicitly call __str__


