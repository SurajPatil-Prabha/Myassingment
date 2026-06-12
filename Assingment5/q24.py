class Product:
    def __init__(self, name):
        self.name = name

class Mobile(Product):
    pass

m = Mobile("iPhone")
print(m.name)