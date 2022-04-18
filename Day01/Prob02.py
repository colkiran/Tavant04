
cntr = 0
for i in range(150, 50, -1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
        cntr += 1

print(f"\nThere are {cntr} prime numbers between 150 and 50")


"""
import math
count=0
for i in range(50,151):
    flag=0
    for j in range(2,int(math.sqrt(i)+1)):
        if i%j==0:
            flag=1
            break
    if flag==0:
        print(i)
        count+=1

print(count)

"""