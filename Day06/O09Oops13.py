
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return f"The price is :{self.__price}"

    def set_price(self, val):
        if val <= 0:
            raise ValueError("Price cannot be negative...")
        else:
            self.__price = val

import sys
try:
    p1 = Product(50)
    print(p1.get_price())
    p1.set_price(100)
    print(p1.get_price())
    # p1.set_price(-10)

except ValueError:
    print("Exception occured....")
    print(sys.exc_info()[0])                    # error
    print(sys.exc_info()[1])                    # message

