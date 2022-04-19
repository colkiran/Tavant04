
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 4, 5]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
l4 = [1, 2, 3, 4, 'five', 'six', 'seven', 'eight', 9.5, 10.2, 11.8, True, False, 14+3j, 15-4j]
print(f"l4 :{l4}")

print(f"l4[0] :{l4[0]}")
print(f"l4[6] :{l4[6]}")
print(f"l4[12] :{l4[12]}")
print(f"l4[14] :{l4[14]}")

print("-" * 40)
l5 = [1, 2, 3, 4, 5]
print(f"l5 :{l5}")
l5[2] = 33
l5[4] = 505
print(f"l5 :{l5}")
# l5[5] = "250"
# print(f"l5 :{l5}")

print("-" * 40)
l6 = [1, 2, 3, 4, 5]
l7 = [6, 7, 8, 9, 10]
print(f"l6 :{l6}")
print(f"l7 :{l7}")
l8 = l6 + l7

print(f"l8 :{l8}")

print("-" * 40)
l5 = list(range(1, 16))
print(f"l5 :{l5}")
for i in l5:
    print(i, end=" ")
print()

print("-" * 40)
print(f"l5 :{l5}")
del l5[9]
print(f"l5 :{l5}")

print("-" * 40)
values = list(range(10, 31, 10))
print(f"values :{values}")

a, b, c = values
print(a, b, c)

print("-" * 40)
a, *b, c = values
print(a, b, c)

*a, b, c = values
print(a, b, c)

a, b, *c = values
print(a, b, c)

# values = [10, 20]
# a, b ,c = values
# print(a, b, c)

print("-" * 40)

l1  = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [l1, l2]
print(f"l3 :{l3}")

l4 = [*l1, *l2]         # unpacking the list
print(f"l4 :{l4}")

print("-" * 40)
vowels = ['a', 'e', 'i', 'o', 'u']
print(f"vowels :{vowels}")
print(list(enumerate(vowels)))

print("-" * 40)
for let in vowels:
    print(let, end=" ")
print()

print("-" * 40)
for let in enumerate(vowels):
    print(let, end=" ")
print()

print("-" * 40)
for let in enumerate(vowels):
    print(let[0], let[1])

print("-" * 40)
for index, let in enumerate(vowels):
    print(index, let)

print("-" * 40)
print(dir(l1))