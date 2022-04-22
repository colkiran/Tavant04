
lst = [1, 2, 3]
print(f"lst :{lst}")
print(type(lst))

print("-" * 40)
# print(dir(lst))
itrObj = lst.__iter__()
# itrObj = iter(lst)

print(f"itrObj :{itrObj}")
print("-" * 40)
print(dir(itrObj))          # __iter__ and __next__, protocol of iterators

print("-" * 40)
print(itrObj.__next__())
print(itrObj.__next__())
print(itrObj.__next__())
# print(itrObj.__next__())                # StopIteration

print("-" * 40)
for i in lst:
    print(i, end=" ")
print()

