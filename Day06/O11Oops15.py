
class Product:

    def __init__(self, price):
        self.__price = price

    @property
    def price(self):
        print("Getter called.....")
        return f"The price is :{self.__price}"

    @price.setter
    def price(self, val):
        print("Setter called.....")
        self.__price = val

    @price.deleter
    def price(self):
        print("deleter called.....")
        self.__price = 0


coke = Product(65)
print(coke.price)

del coke.price
print(coke.price)

coke.price = 100
print(coke.price)
