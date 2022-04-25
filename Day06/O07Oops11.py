
class Employee:

    def __init__(self, name):
        self.name = name
        self.tech = ['c++', 'C#', 'asp.net', 'vb.net', 'angular', 'react']

    def __str__(self):
        return "{} and {}".format(self.name, self.tech)

    def __len__(self):
        return len(self.tech)

    def __iter__(self):
        return iter(self.tech)  # self.tech.__iter__()

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, value):
        self.tech[index] = value


emp1 = Employee("Richards")
print(emp1)
print("-" * 40)

emp1.append("Python")

print([tech for tech in emp1.tech])

print("-" * 40)

x = emp1[3]
print(f"x :{x}")

print("-" * 40)

emp1[3]  = 'sql server'
print([tech for tech in emp1.tech])