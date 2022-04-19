
# c style formatting
format = "Welcome %s, what a %s player"
print(format)
values = ("Sachin", "class")            # tuple
print(values)

print(format % values)

print("-" * 40)
format = "Welcome %s, your rating of %.3f what a player"
print(format)
print(format % ("Sachin", 4.9))
print(format % ("Rahul", 4.783))
print(format % ("Rahul", 4.783346323))
print("-" * 40)
print("Welcome %s, your rating of %.3f what a player" % ("Sachin", 4.89))


print("-" * 40)
# unix style
from string import Template
tmpl = Template("Welcome $name, what a $adjective player")
print(f'tmpl :{tmpl}')
res = tmpl.substitute(name="Sachin", adjective="superb")
print(res)

print("-" * 40)
# format strings from python
print("Welcome {}, what a {} player".format("Sachin", "superb"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "superb", "India"))
print("Welcome {name}, what a {adj} player for {ctry}".format(name="Sachin", adj="superb", ctry="India"))
print("Welcome {name} your rating of {rating} what a  player".format(name="Sachin", rating=4.8))
print("Welcome {name} your rating of {rating:.2f} what a  player".format(name="Sachin", rating=4.8))

print("-" * 40)
# interpolation
from math import pi, e
print(f"PI={pi} and Eulers={e}")

print("PI = {} and Eulers constant = {}".format(pi, e))
print("PI = {} and Eulers constant = {} and magic number is {}".format(pi, e, 40585))

print("Conversions".center(40, "-"))
print("{val} {val} {val}".format(val="A"))
print("{val!s} {val!r} {val!a}".format(val="A"))

print("-" * 40)
print("The number {num} {num} {num}".format(num = 36))
print("The number {num} {num:f} {num:b}".format(num = 36))
print("The number {num:10} {num:f} {num:b}".format(num = 36))
print("The number {num:5} {num:f} {num:b}".format(num = 36))
print("The number {num:5} {num:f} {num:b}".format(num = 36344566756))

print("-" * 40)
print("{num:10}Tendulkar".format(num=3))
print("{num:10}Tendulkar".format(num="Sachin"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

print("Alignment".center(40, "-"))
print("{fname:15} Tendulkar".format(fname="Sachin"))
print("{fname:>15} Tendulkar".format(fname="Sachin"))
print("{fname:^15} Tendulkar".format(fname="Sachin"))
print("{fname:<15} Tendulkar".format(fname="Sachin"))

print("{fname:-^25}".format(fname="Sachin"))
print("{fname:#^30}".format(fname=45000))

print("{}".format(10 ** 100))
print("{:,}".format(10 ** 100))
