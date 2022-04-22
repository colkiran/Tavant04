
def outerFun(greet):
    def innerFun(name):
        print(greet, name)

    return innerFun

outerFun("Welcome")("Sachin")

# simple curry
engGreet = outerFun("Welcome")
hindiGreet = outerFun("Namaskar")
tamilGreet = outerFun("Vanakam")

engGreet("Sachin")
hindiGreet("Rahul")
tamilGreet("Dhoni")
