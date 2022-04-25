
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):

    def doJob(self):
        print("Manager's Job......")

class Developer(Employee):

    def doJob(self):
        print("Developers job.......")

def BankFun(emp):       # polymorphism

    print("Bank job started".center(40, "-"))
    emp.doJob()
    print("Bank job ended".center(40, "-"))
    print("-" * 40)


Mike = Manager()
David = Developer()

BankFun(Mike)
BankFun(David)

print("-" * 40)

def BankFunJobs(emps):       # polymorphism

    print("Bank job started".center(40, "-"))
    for emp in emps:
        emp.doJob()
    print("Bank job ended".center(40, "-"))
    print("-" * 40)

BankFunJobs([Mike, David])
