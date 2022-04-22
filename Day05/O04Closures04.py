
def outerFun(greet):
    def innerFun(sep):
        def innerMostFun(name):
            import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + name)
            print(emojized)
        return innerMostFun
    return innerFun

kanGreet = outerFun("Namaskara")
tigerEmj = kanGreet("tiger")
tigerEmj("Prabhakar")

print("-" *  40)

engGreet = outerFun("Welcome")
elpntEmj = engGreet("elephant")
elpntEmj("Babu")


"""
outerFun("Welcome")("---->")("Sourav")

engGreet = outerFun("Welcome")
spnGreet = outerFun("Hola")

dblLine = engGreet("=====>")
starLine = spnGreet("******>")

dblLine("Suresh")
starLine("Messi")

"""