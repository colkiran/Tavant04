
class Greet:

    def __init__(self, fnc):                # constructor
        self.fnc = fnc

    def __call__(self, *args):
            self.fnc(*args)

@Greet
def fun(x, y):
    print(f"Happy weekend {x}, {y}")


fun("David", "Mike")
