
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


    def __str__(self):
        return "{} and {}".format(self.name, self.salary)

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return  self.salary // other.salary

emp1 = Employee("Kevin", 25000)
emp2 = Employee("Alex", 20000)

print(emp1)
print("-" * 40)
print(emp2)

print("-" * 40)
print("Add :", emp1 + emp2)

print("-" * 40)
print("Subtract :", emp1 - emp2)

print("-" * 40)
print("Multiply :", emp1 * emp2)

print("-" * 40)
print("Divide :", emp1 / emp2)

print("-" * 40)
print("Floor Division :", emp1 // emp2)
