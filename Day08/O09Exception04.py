
class NotEqual(Exception):
    pass

class L1Greater(Exception):
    pass

class L1Smaller(Exception):
    pass


l1 = [1, 2, 3]
l2 = [3, 2, 1]

try:
    if l1 > l2:
        raise L1Greater("L1 is greater than l2")
    elif l1 < l2:
        raise L1Smaller("l1 is smaller than l2")
    elif l1 != l2:
        raise NotEqual("L1 is not equal")
    else:
        print("Both are equal.....")
except NotEqual as ne:
    print(ne)
except L1Greater as gr:
    print(gr)
except L1Smaller as sm:
    print(sm)
finally:
    print("completed comparing lists....")