
class Employee:
    def __init__(self, name):
        self.__name = name              # private variable, cannot be accessed outside the class
        self.tech = ['c++', 'C#', 'asp.net', 'vb.net', 'angular', 'react']

    def __str__(self):
        return  "Name is :" + self.__name + " and tech is :" + ",".join([tech for tech in self.tech])


emp1 = Employee("Micheal")
print(emp1)

print("-" * 40)
# print(emp1.__name)
print(emp1.__dict__)
emp1._Employee__name = "Louis"
print(emp1.__dict__)
