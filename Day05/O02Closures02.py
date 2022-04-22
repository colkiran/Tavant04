
# closure
def outerFun(info):                     # HOF - Higher Order Function
    inf = "Mr." + info

    def innerFun():
        print(inf)

    return innerFun

outerFun("Virat")
print("-" * 40)

print(outerFun.__name__)
print(outerFun("sachin").__name__)

print("-" * 40)
inRef = outerFun("Virat")
inRef()

print("-" * 40)
outerFun("Virat")()         # calls the inner function

print("-" * 40)
inRef = outerFun("Dhoni")

print("before the inner fun call")
print("before the inner fun call")
print("before the inner fun call")
print("before the inner fun call")

inRef()
