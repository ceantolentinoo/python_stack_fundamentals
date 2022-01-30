from product import *
class Store:
    def __init__(self, name, products = []):
        self.name = name
        self.products = products

    def add_product(self, new_product):
        self.products.append(new_product)
        print("Product added!")
        return self

    def sell_product(self, id):
        self.products.pop(id)
        print("Product sold!")
        return self

    def inflation(self, percent_increase):
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for i in range(len(self.products)):
            if(self.products[i].category==category):
                self.products[i].update_price(percent_discount, False)


costco = Store("Costco")
print(costco.add_product(Product("Coca-cola", "Soda", 1.99)).add_product(Product("Aged Cheddar", "Cheese", 5.99)).add_product(Product("Jeans", "Clothing", 120)).add_product(Product("Sprite", "Soda", 1.99)))

costco.set_clearance("Soda", 0.5)

for i in range(len(costco.products)):
    print(costco.products[i].print_info())