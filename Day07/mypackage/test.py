

class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name :{self.name}\nAge :{self.age}")


emp1 = Employee("Jack", 30)
emp1.get_details()

