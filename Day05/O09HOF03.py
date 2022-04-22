
def funLogger(fnc):
    def helper():
        print("My Info logged in  a service...")
        fnc()
        print("My Info logged out of service")
    return helper

def normalfun():
    print("I have called normal function.....")

funLogger(normalfun)                # no output
print("-" * 40)
funLogger(normalfun)()
print("-" * 40)
res_fun = funLogger(normalfun)
res_fun()

print("-" * 40)
@funLogger                      # decorator
def basicFun():
    print("I have called basicFun....")

# basicFun = funLogger(basicFun)
# basicFun()

basicFun()