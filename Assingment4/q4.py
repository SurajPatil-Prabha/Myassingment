class Mobile:
    discount_percentage = 10

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_mobile(self):
        print("\nBrand:", self.brand)
        print("Model:", self.model)
        print("Price:", self.price)

    def calculate_discount_price(self):
        discount = (self.price * Mobile.discount_percentage) / 100
        final_price = self.price - discount
        print("Price After Discount:", final_price)

    @classmethod
    def change_discount(cls, new_discount):
        cls.discount_percentage = new_discount


mobile1 = Mobile("Samsung", "S24", 80000)
mobile2 = Mobile("OnePlus", "12R", 45000)

mobile1.display_mobile()
mobile1.calculate_discount_price()

Mobile.change_discount(15)

print("\nNew Discount Percentage:", Mobile.discount_percentage)

mobile2.display_mobile()
mobile2.calculate_discount_price()