
class Animal:

    def eat(self):
        print("Animals eat......")

class Bird(Animal):

    def fly(self):
        print("Birds fly.......")

class Chicken(Bird):

    def eggs(self):
        print("Chicken eggs has a lot of protien......")

chick = Chicken()
chick.eat()
chick.fly()
chick.eggs()
