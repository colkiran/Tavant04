
import O06BankModule

def withdraw(self):
    print("You can withdraw upto 4k per day.........")


O06BankModule.HDFC.withdraw = withdraw          # monkey patching

hdfc = O06BankModule.HDFC()
hdfc.withdraw()

