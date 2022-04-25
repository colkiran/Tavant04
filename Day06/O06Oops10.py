
class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['c++', 'C#', 'asp.net', 'vb.net', 'angular', 'react']

    def __str__(self):
        return "{} and {}".format(self.name, self.salary)

    def __add__(self, other):
        return self.salary + other.salary

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)          # self.tech.__iter__()


emp1 = Employee("Peter", 50000)
print(emp1)
print("-" * 40)

print(len(emp1))
print("-" * 40)

print([t for t in emp1])
print("-" * 40)
