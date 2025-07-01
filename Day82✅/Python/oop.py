class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        return f"{self.name} - PKR {self.price}"

p1 = Product("Camera", 50000)
print(p1.show())