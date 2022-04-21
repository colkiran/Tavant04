
glbx = 100


def fun(n):             # local
    n += 10
    print(f"n :{n}")
    print(f"glbx :{glbx}")
    # glbx = 500

print(f"before :{glbx}")
fun(10)

print(f"glbx after :{glbx}")