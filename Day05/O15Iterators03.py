
class MyNumbers:

    def __init__(self, max):                # constructor
        self.max = max

    def __iter__(self):                     # returns iterable object
        self.n = 2
        return self

    def __next__(self):                     # get the next element
        if self.n <= self.max:
            res = self.n
            self.n += 2
            return res
        else:
            raise StopIteration

myObj = MyNumbers(10)
itrObj = iter(myObj)

print(f'itrObj :{itrObj}')
print(next(itrObj))
print(next(itrObj))
print(next(itrObj))
print("-" * 40)

for i in myObj:
    print(i)
