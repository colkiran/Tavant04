
numbers = [1, 2, 3, 4, 5]
print(f"numbers :{numbers}")
itrObj = iter(numbers)

while True:
    try:
        elem = next(itrObj)
        print(elem)
    except StopIteration:
        break

print("-" * 40)
st = "Hello World"
for s in st:
    print(s, end=" ")
print()

