class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Bike(Vehicle):
    def __init__(self, brand, gear):
        super().__init__(brand)
        self.gear = gear

b = Bike("Honda", 5)
print(b.brand, b.gear)