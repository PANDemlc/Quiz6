# s.py
# Braden Burgener
# CS325 Quiz 6
class Location:
    def __init__(self, address, tax_rate):
        self.address = address
        self.tax_rate = tax_rate

class Customer:
    def __init__(self, name, location, email):
        self.name = name
        self.location = location
        self.email = email

class Item:
    def __init__(self, name, price, discount=0.0):
        self.name = name
        self.price = price
        self.discount = discount

class OrderDetails:
    def __init__(self, customer):
        self.customer = customer
        self.items = []
        self.address = customer.location.address

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items
    
class OrderTotal:
    def __init__(self, order):
        self.customer = order.customer
        self.items = order.items
        self.tax_rate = order.customer.location.tax_rate
        self.order = order

    def calc_total(self, items):
        subtotal = sum(item.price for item in self.order.items)
        for item in self.order.items:
            subtotal -= (item.price * item.discount)
        tax = subtotal * self.tax_rate
        return subtotal + tax
    
class Stock:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.stock = []

    def check_stock(self, items):
        temp_stock = self.stock
        for item in items:
            for stock in temp_stock:
                if stock.name == item.name:
                    if stock.quantity > 0:
                        stock.quantity -= 1
                        return True
                    else:
                        return False
            else:
                return False
    
    def remove_stock(self, items):
        for item in items:
            for stock in self.stock:
                if stock.name == item.name:
                    if stock.quantity > 0:
                        stock.quantity -= 1
                        return True
                else:
                    return False
            else:
                return False

    def add_stock(self, new_stock):
        stockFound = False
        for stock in self.stock:
            if stock.name == new_stock.name:
                stock.quantity += new_stock.quantity
                stockFound = True
        if not stockFound:
            self.stock.append(new_stock)

class OrderEmail:
    def __init__(self, order):
        self.order = order
    
    def confirmation_email(self):
        print(f"Confirming with {self.order.customer.email}")
    
def main():
    siue = Location("SIUE", 0.1)
    bradenb = Customer("Braden B", siue, "braburg@siue.edu")
    newOrder = OrderDetails(bradenb)

    # Name, Price, Discount
    game = Item("New Game", 59.99, 0.15)
    newOrder.add_item(game)

    inventory = Inventory()
    stock = Stock("New Game", 5)
    inventory.add_stock(stock)

    price = OrderTotal(newOrder)
    print(f"Order total was {price.calc_total(newOrder.get_items())}")

    if inventory.check_stock(newOrder.get_items()):
        inventory.remove_stock(newOrder.get_items())
        email = OrderEmail(newOrder)
        email.confirmation_email()
    else:
        print("No stock")
    




if __name__ == "__main__":
    main()