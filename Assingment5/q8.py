class Product:
    tax_rate = 0.18

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price + (self.price * Product.tax_rate)

p = Product(1000)
print(p.final_price())