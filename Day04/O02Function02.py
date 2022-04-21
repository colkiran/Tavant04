
# Named Tuple
from collections import  namedtuple

def arithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    nmdtpl = namedtuple("ArithmeticCalc", "sum diff prod quot")
    res = nmdtpl(sum = sum, diff = diff, prod=prod, quot=quot)
    return res

res1 = arithmeticCalc(20, 6)
print(f"res1       :{res1}")
print(f"Sum        :{res1.sum}")
print(f"Difference :{res1.diff}")
print(f"product    :{res1.prod}")
print(f"quotient   :{res1.quot}")

# varaible length arguments
# *arg -  accept data in the form of a tuple

print("-" * 40)
def productAll(*numbers):
    print(numbers)
    print(*numbers)     # unpacking
    prod = 1
    for num in numbers:
        prod *= num
        return prod

productAll(1, 2, 3, 4, 5)

def extractDetails(**details):
    print(details)
    print("Name :", details['name'])

extractDetails(name="Sachin", runs=125, oppon="WI", venue="sabina park")

print("-" * 40)

def recruit(name, *tech,  **marks):
    print(f"Name :{name}")
    print("Technologies :", tech)
    print("Marks :", marks)


recruit("Kevin", "C++", "Dotnet", "C#", "asp.net", "sqlserver", 'Angular', Xth = "83%", XIIth = '87%',
        degree = "75%", pg= '94%')

print("-" * 40)
# document a function
def fun():
    "This is a simple string"
    # this is a comment
    print("hello World")

fun()
print(fun.__doc__)

print("-" * 40)

def fun1(x, y):
    """
        This function fun1 is a simple function which takes two int as arguments

        res = fun1(x as int, y a int)

        The function takes two integers and returns an integer as a result
        if we pass two string values to the function it will cocatenate and return the values
    """
    return x ** y

print(fun1(2,3))

print("-" * 40)

help(fun1)
