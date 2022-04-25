
# duck types

class Manager:
    def doJob(self):
        print("Manager Job.....")

class Developer:
    def doJob(self):
        print("Developers Job.....")

Mike = Manager()
David = Developer()

def BankFunJobs(emps):       # polymorphism

    print("Bank job started".center(40, "-"))
    for emp in emps:
        emp.doJob()
    print("Bank job ended".center(40, "-"))
    print("-" * 40)

BankFunJobs([Mike, David])
