
def greet():
    print("Greetings Mr. Sachin, Welcome to the event...")


def greetGuest(gname):
    print(f"Greetings Mr. {gname}, Welcome to the event.....")

# city is called default argument, gname is called non default argument
def greetGuestCity(gname, city = "Mumbai"):
    print(f"Greetings Mr. {gname} from {city}, Welcome to the event.....")


greet()
greetGuest("Rahul")
greetGuestCity("Sachin")
greetGuestCity("Rohit")
greetGuestCity("Dhoni", "Ranchi")

print("-" * 40)
def admsn(fname, lname, dob, city, contno, qlf, adhrno):
    print(f"Name :{fname} {lname}" )
    print(f"dob :{dob}")
    print(f"city :{city}")
    print(f"contact no :{contno}")
    print(f"Qualification :{qlf}")
    print(f"Adhar No :{adhrno}")


admsn(city = "New Delhi", qlf = "Mtech", adhrno='2346DSFSD3', fname='Virat',
      lname='Kholi', dob="34/10/9185", contno='324246312')

print("-" * 40)

def addMe(x, y):
    return x + y

print(addMe(10, 20))

# recursive calls
def fun(n):
    if n == 0:
        return 1
    else:
        return fun(n - 1)

print(fun(10))

print("-" * 40)

def fun(n):
    if n == 0:
        return 1
    return n*fun(n-1)

x = 5
print(f"The factorial of {x} is :{fun(x)}")

print("-" * 40)
def fib(n):
     if n <= 1:
         return n
     else:
         return fib(n - 1) + fib(n - 2)

n = int(input("Enter the no of iterations"))
for i in range(n):
    print(fib(i), end=" ")
print()

