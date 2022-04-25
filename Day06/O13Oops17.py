
class Animal:

    def __init__(self):
        print("Animal Ctor......")
        self.age = 1

    def eat(self):
        print("Animals eat......")

class Bird(Animal):

    def __init__(self):                     # overriding Animal class constructor
        super().__init__()
        print("Bird Ctor.....")
        self.weight = '1 kilo'

    def fly(self):
        print("Birds Fly.......")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print(cuckoo.__dict__)
