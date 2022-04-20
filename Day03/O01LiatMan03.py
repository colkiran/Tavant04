
print("Index".center(40, "-"))
l= [1, 2, 3, 1, 2, 2, 1, 2,1, 2, 2, 1, 1,1,3, 1, 2,1, 2,3]
print(f"l :{l}")
print(f"Index 3 :{l.index(3)}")

print(f"Index 3 :{l.index(3, 4)}")
print(f"Index 3 :{l.index(3, 15)}")

print("Count".center(40, "-"))
l= [1, 2, 3, 1, 2, 2, 1, 2,1, 2, 2, 1, 1,1,3, 1, 2,1, 2,3]
print(f"l :{l}")
print(f"1 :{l.count(1)}")
print(f"2 :{l.count(2)}")
print(f"5 :{l.count(5)}")

print("{x:-^40}".format(x="copy"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 Before :{l1}")
l2 = l1                 # shallow copy - its not only sharing the data but also the address
print(f"l2 Before :{l2}")
l2.extend([6, 7, 8, 9])
print(f"l2 After :{l2}")
print(f"l1 After :{l1}")

print("-" * 40)
l3 = [6, 7, 8, 9, 10]
print(f"l3 Before :{l3}")
l4 = l3.copy()              # deep copy - shares only the data not the addresses
print(f"l4 Before :{l4}")

l4.append(11)
l4.append(12)
l4.append(13)

print(f"l4 After: {l4}")
print(f"l3 After: {l3}")

print("-" * 40)
l5 = [1, 2, 3, 4, [11, 22, 33, 44, 55], 5, 6]
print(f"l5 Before :{l5}")
l6 = l5.copy()
print(f"l6 Before :{l6}")

l6[4].append(66)
l6[4].append(77)
l6[4].append(88)
print(f"l6 After {l6}")
print(f"l5 After {l5}")

print("-" * 40)
from copy import deepcopy
l7 = [10, 20, 30, 40, [1, 2, 3, 4, 5], 60, 70]
print(f"l7 Before :{l7}")
l8 = deepcopy(l7)
print(f"l8 Before :{l8}")

l8[4].extend([6, 7, 8, 9])
print(f"l8  After :{l8}")
print(f"l7  After :{l7}")