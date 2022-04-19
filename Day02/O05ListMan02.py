
"""
'append', 'clear', 'copy', 'count', 'extend',
 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""

# add new values into the list

print("{text:-^40}".format(text="append"))
l1 = list(range(10, 101, 10))
print(f"l1 :{l1}")

l1.append(110)
l1.append(120)
l1.append(130)
print(f"l1 :{l1}")

l1.append([140, 150, 160, 170])
print(f"l1 :{l1}")
print(l1[13][1:3])

print("extend".center(40, "-"))
l2 = [1, 2, 3, 4, 5]
print(f"l2 :{l2}")
l2.extend([6, 7, 8])
l2.extend([9, 10, 11])
print(f"l2 :{l2}")

print("{text:-^40}".format(text="insert"))
l1 = [1, 2, 3, 4, 5]
l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
print(f"l1 :{l1}")

# delete values from a list
# pop, remove

print("pop".center(40, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = l1.pop(4)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

print("remove".center(40, "-"))
l1 = [1, 2, 1, 2, 3, 1, 1, 1, 3, 1, 2, 1, 2, 1, 2, 1, 3, 4, 1, 1, 2, 1, 1, 1]
print(f"l1 :{l1}")
l1.remove(1)
print(f"l1 :{l1}")

