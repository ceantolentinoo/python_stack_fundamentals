import uuid
class Product:
    def __init__(self, name, category, price):
        self.id =uuid.uuid1()
        self.name = name
        self.category = category
        self.price = price

    def update_price(self, percent_change, is_increased):
        if(is_increased):
            self.price = (self.price*percent_change) + self.price
            return "Price Increased!"
        else:
            self.price = -(self.price*percent_change) + self.price
            return "Price Decreased!"

    def print_info(self):
        return ("ID: {} | Name: {} | Category: {} | Price: {}").format(self.id, self.name, self.category, self.price)
