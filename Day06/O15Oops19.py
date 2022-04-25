
class Animal:
    def __init__(self):
        self.a = 10
        print("Animal Ctor....")

    def eat(self):
        print("Animals eat......")

    def fun(self):
        print("Fun method of Animal class......")

class Person:
    def __init__(self):
        self.p = 20
        print("Person Ctor.......")

    def talk(self):
        print("Person Talk......")

    def fun(self):
        print("Fun method of Person class.....")

class Girl(Animal, Person):
    def __init__(self):
        super().__init__()
        Person.__init__(self)
        self.g = 30
        print("Girl Ctor.......")

Jenni = Girl()
Jenni.eat()
Jenni.talk()
Jenni.fun()

print(Jenni.__dict__)
