

def fun1(*args):
    print(args)
    print(*args)
    print("-" * 40)

fun1()
fun1(20)
fun1(10, 20, 30, 40, 50)

def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

def log_details(fnc):                       # HOF
    logIn = "Logging into the service...."
    logOut = "Logging out of the service....."

    def innerFun(*args):
        print(logIn)
        print(fnc(*args))
        print(logOut)
        print("-" * 40)

    return innerFun

sum_logger = log_details(sum)
diff_logger = log_details(diff)

sum_logger(345, 686)
diff_logger(934, 752)

