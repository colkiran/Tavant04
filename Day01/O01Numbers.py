
a = 10
b = -10
print(f"a :{a}")
print(type(a))                      # RTTI = Runtime Type Identification
print(f"b :{b}")
print(type(b))

print("-" * 40)
c = 5.8
d = -5.8
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 40)
e = 2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 40)
g = 3 + 4j
h = 3 - 4j
print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 40)
print(3 + 4.5)

x = 3
y = 4.5
z = x + y

print("x =", type(x))
print("y =", type(y))
print("z =", type(z))

print("conversions".center(40, "-"))
a = -10
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number system".center(40, "-"))
print(11)           # decimal
print(0b11)         # binary
print(0b101)        # binary
print(0o11)         # octal
print(0o15)         # octal
print(0xe)          # hexa
print(0xa)          # hexa


print("Number system conversion".center(50, "-"))
a = 100
print(f"a :{a}")
print("oct :", oct(a))
print("hex :", hex(a))
print("bin :", bin(a))
