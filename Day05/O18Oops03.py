
class Player:

    def __init__(self):
        self.name = "Sachin"
        self.age = 38
        print("Player Initialized......")

    def get_details(self):
        print(f"name = {self.name}\nAge = {self.age}")

ply1 = Player()
ply1.get_details()
print("-" * 40)

ply2 = Player()
ply2.name = "Rahul"
ply2.age = 35
ply2.get_details()

