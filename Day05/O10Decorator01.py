
def funLogger(fnc):
    def helper(x, y):
        print("My info logged into the service....")
        res = fnc(x, y)
        print("My Info logged out of the service......")
        return res
    return helper

@funLogger
def add(x, y):
    print("Add called...")
    return x + y

@funLogger
def sub(x, y):
    print("Sub called.....")
    return x - y

@funLogger
def mul(x, y):
    print("Mul called.....")
    return x * y

res = add(2,3)
print("-" * 40)
print(f"res :{res}")

print("-" * 40)
print(sub(40, 25))

print("-" * 40)