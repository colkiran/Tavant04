
def bank_flow(fnc):
    print("-" * 40)
    print("login to the server")
    fnc()                           # callback
    print("logout of the server")
    print("-" * 40)


def deposit():
    print("credited....")

def withdraw():
    print("debited......")

bank_flow(deposit)
bank_flow(withdraw)
