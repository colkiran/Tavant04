
def doubleMesh(fnc):
    def helper(*args):
        print("#" * 40)
        fnc(*args)
        print("=" * 40)

    return helper

def starSingle(fnc):
    def helper(*args):
        print("*" * 40)
        fnc(*args)
        print("-" * 40)
    return helper

@starSingle
@doubleMesh
def fun():
    print("fun called....")

@starSingle
@doubleMesh
def fun1(x):
    print("fun1 called...", x)

@starSingle
@doubleMesh
def fun2(x, y):
    print("fun2 called.....", x, y)


fun()
fun1(10)
fun2(20, 30)


# fun3(30, 40, 50)
# fun4(10, 20, 30, 40, 50)
