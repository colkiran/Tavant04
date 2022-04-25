
from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self):
        print("Account")

    @abstractmethod
    def getBalance(self):
        pass

    def deposit(self):
        print("Credited......")


class Savings(Account):
    def withdraw(self):
        print("Debied........")

    def getBalance(self):
        print("Balance in the account is #####.##")


sav = Savings()
sav.withdraw()
