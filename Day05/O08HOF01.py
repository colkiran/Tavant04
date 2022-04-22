
def callMe():
    print("Apples from Ooty.....")

def fun(fnc):
    print("Hello......")
    fnc()
    print("Hi.......")

    def defineMe():
        print("Oranges from Kanpur.....")

    return defineMe

def funCallback(fnc):
    print("India in great......")
    fnc()
    print("Mera baharath mahan.......")

funCallback(fun(callMe))
