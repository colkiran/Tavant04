
from sys import getsizeof

val1 = sum([x ** 2 for x in range(1, 11)])               # comprehension
print(val1)
print(type(val1))

val2 = sum((x ** 2 for  x in range(1, 11)))              # generator
print(val2)
print(type(val2))

print("-" * 40)

val3 = [x ** 2  for x in range(1, 10000)]

val4 = (x ** 2 for x in range(1, 10000))

print(f"Comprehension size of lst :", getsizeof(val3))
print(f"Generator size of lst :", getsizeof(val4))
