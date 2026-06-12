class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show(self):
        print(self.brand, self.price)

m = Mobile("Samsung", 20000)
m.show()