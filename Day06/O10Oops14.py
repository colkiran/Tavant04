
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        print("Getter called.....")
        return f"The price is :{self.__price}"

    def set_price(self, val):
        print("Setter called.....")
        self.__price = val

    def del_price(self):
        print("deleter called.....")
        self.__price = 0

    price = property(get_price, set_price, del_price)

pepsi = Product(42)
x = pepsi.price
print(f"x :{x}")

pepsi.price = 85
print(pepsi.price)

del pepsi.price
print(pepsi.price)
