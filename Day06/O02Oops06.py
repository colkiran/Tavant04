
class Player:
    team = "India"

    def __init__(self, name, age):                  # constructor
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name :{self.name}\nAge :{self.age}")

    @classmethod
    def CreatePlayer(cls, fname, lname, age):               # cls - class name
        print("Factory...")                                 # factory
        return cls(f"Mr.{fname} {lname}",age)                      # calls the constructor

ply1 = Player("Sachin", 38)
ply1.get_details()

print("-" * 40)
ply2 = Player.CreatePlayer("Virat", "Kholi", 26)
ply2.get_details()


