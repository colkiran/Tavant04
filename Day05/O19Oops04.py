"""
self will have the name of the object that called the method

"""
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized......")

    def get_details(self):
        print(f"name = {self.name}\nAge = {self.age}")

ply1 = Player("Sachin", 36)
ply1.get_details()

print("-" * 40)

ply2 = Player("Rahul", 34)
ply2.get_details()

print("-" * 40)
print(ply1.__dict__)
print(ply2.__dict__)

print("-" * 40)
ply2.runs = 85
print(ply1.__dict__)
print(ply2.__dict__)
