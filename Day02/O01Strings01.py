

st = "hello world"
print(f"st :{st}")
print(type(st))

print("-" * 40)
st = "Hello World"
print(f"st :{st}")
print(st[0])            # indexing
print(st[6])
print(st[10])

#slicing
print("-" * 40)
print(st[0:5])
print(st[6:11])
print(st[0:11])
print(st[0:11:2])
print(st[0:])
print(st[:11])
print(st[:])

# Reverse Indexing
print("-" * 40)
print(st[-1])
print(st[-5])
print(st[-11])

# slicing
print(f"st[-1:-6:-1] :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1] :{st[-1::-1]}")
print(f"st[::-1] :{st[::-1]}")

# strings are immutable
st = "Hello world"
print(f"st[6] :{st[6]}")
# st[6] = "W"

print("-" * 40)
print(dir(st))
