
for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 40)
for j in range(1, 20):
    # if  j > 15:
    #     break
    if j % 2 == 1:
        continue
    print(j, end=" ")
else:
    print("\nFor loop completed")

print(f"j :{j}")

