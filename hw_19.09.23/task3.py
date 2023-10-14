class Product:
    def __init__(self, type_product, name, price):
        self.type_product = type_product
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.type_product}:{self.name}:{self.price}"


class ProductStore:

    def __init__(self):
        self.storage = {}
        self.income = 0

    def add(self, product, amount):
        product.price *= 1.3
        self.storage[product.name] = {
            "type": product.type_product,
            "price": product.price,
            "amount": amount
        }

    def set_discount(self, identifier, percent, identifier_type='name'):
        for product, amount in self.storage.items():
            if product.type_product == identifier_type or product.name == identifier:
                product.price *= (1 - percent / 100)

            print("There is no such product")

    def sell_product(self, product_name, amount):
        if product_name in self.storage:
            if self.storage[product_name]['amount'] >= amount:
                self.storage[product_name]['amount'] -= amount
                self.income += amount * self.storage[product_name]["price"]
            else:
                raise ValueError(f"there is not enough goods: {self.storage[product_name]}")
        else:
            raise ValueError("Not found")

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.storage

    def get_product_info(self, product_name):
        if product_name in self.storage:
            return product_name, self.storage[product_name]["amount"]

        else:
            raise ValueError(f"{product_name} not found")


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
