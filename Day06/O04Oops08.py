
class Player:
    team = "India"

    def __init__(self, name, salary):                  # constructor
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name :{self.name}\nAge :{self.salary}"

    def __eq__(self, other):                    # works for not equal to also
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary

ply1 = Player("David", 45000)
print(ply1)

print("-" * 40)
ply2 = Player("Tony", 55000)
print(ply2)

print("-" * 40)
print(ply1 == ply2)                         # compare the addresses by default

if ply1 == ply2:
    print("{} salary of {} is equal to {} salary of {}".format(ply1.name, ply1.salary,
                                                                ply2.name, ply2.salary))
else:
    print("{} salary of {} is NOT equal to {} salary of {}".format(ply1.name, ply1.salary,
                                                                ply2.name, ply2.salary))

if ply1 != ply2:
    print("{} salary of {} is NOT equal to {} salary of {}".format(ply1.name, ply1.salary,
                                                                ply2.name, ply2.salary))
else:
    print("{} salary of {} is equal to {} salary of {}".format(ply1.name, ply1.salary,
                                                                ply2.name, ply2.salary))
print("-" * 40)

if ply1 > ply2:
    print("{} salary of {} is greater than {} salary of {}".format(ply1.name, ply1.salary,
                                                                ply2.name, ply2.salary))
else:
    print("{} salary of {} is greater than {} salary of {}".format(ply2.name, ply2.salary,
                                                                ply1.name, ply1.salary))

print("-" * 40)

if ply1 < ply2:
    print("{} salary of {} is less than {} salary of {}".format(ply1.name, ply1.salary,
                                                                ply2.name, ply2.salary))
else:
    print("{} salary of {} is less than {} salary of {}".format(ply2.name, ply2.salary,
                                                                ply1.name, ply1.salary))
