
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 40)
t2 = tuple(range(1, 11))
print(f"t2 :{t2}")
print(type(t2))

print("-" * 40)
t3 = (1, 2, 3, 4, 5)
print(f"t3 :{t3}")
print(type(t3))

print("-" * 40)
t4 = 10,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 40)
t5 = 10, 20, 30, 40, 50
print(f"t5 :{t5}")
print(type(t5))

#tuples are immutable
t1 = (1, 2, 3, 4, 5)
print(t1[3])
# t1[3] = 44

# print(dir(t1))

print("-" * 40)
t1 = (1, 2, 3 , 1, 2, 1, 2, 3, 1, 1, 2, 1, 2, 1, 2, 4, 3)
print(f"t1 :{t1}")

# count
print("1 :", t1.count(1))
print("2 :", t1.count(2))

# index
print(t1.index(3))
print(t1.index(3, 3))
print(t1.index(3, 8))