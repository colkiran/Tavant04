"""
arithmetic
Comparison or relational
Logical
Bitwise
Ternary
"""

print("Arithmetic Operators".center(40,"-"))
print(10 + 3)           # add
print(10 - 3)           # sub
print(10 * 3)           # multi
print(10 / 3)           # div
print(10 // 3)          # floor div
print(10 % 3)           # mod
print(10 ** 3)          # power(super script)

print("Augmentor Operators".center(40, "-"))
# =, +=, -=, /=, *=
x = 10
print(f"x :{x}")
x += 3          # x = x + 3
print(f"x :{x}")
x -= 1
print(f"x :{x}")
x /= 3
print(f"x :{x}")

print("Comparison Operator".center(40, "-"))
a = 10
b = 20
print(a == b)
print(b == a)
print(a <= b)
print(b >= a)

print("Logical Operators".center(40, "-"))
print(1 == 1 and 2 == 2)
print(1 == 1 and 1 == 2)

print(1 == 1 or 2 == 1)
print(1 == 2 or 2 == 2)

print(not(1 == 1 or 2 == 1))
print(not(1 == 1 and 1 == 2))

print("ascii values".center(40, "-"))
print("a =",ord("a"))
print("z =", ord("z"))
print("A =", ord("A"))
print("Z =", ord("Z"))
print("apple" > "orange")
print("orange" > "apple")

print("Bitwise Operators".center(40, "-"))
print(5 | 3)
print(5 & 3)
print(5 ^ 3)
print(5 << 1)
print(5 >> 1)
print(8 >> 1)

print(~0)
print(~5)

# ternary operator
a = 15
print("Eligible" if a > 18 else "not eligible")