
l1 = [1, 2, 1, 2, 3, 1, 1, 1, 3, 1, 2, 1, 2, 1, 2, 1, 1, 1, 1, 1, 3, 4, 1, 1, 2, 1, 1, 1]

while True:
    try:
        l1.remove(1)
    except ValueError:
        break

print(f"l1: {l1}")