

glbx = 100                  # global variable

def fun(n):                 # local variable
    global glbx             # we cannot assing a value to the varible
    n += 10
    print(f"n :{n}")
    y = n // 2              # local variable
    print(f"y :{y}")
    glbx = 500              # local variable
    print(f"Inside :{glbx}")

print(f"before :{glbx}")

fun(20)

print(f"After :{glbx}")
