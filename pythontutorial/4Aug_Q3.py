"""Q3: Write a Python class Inventory with attributes like item_id, item_name,
stock_count,and price, and methods like add_item, update_item, and check_item_details.
Use a dictionary to store the item details, where the key is the item_id and the value is a d
ictionary containing the item_name, stock_count, and price."""


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_id, item_name, stock_count, price):
        self.items[item_id] = {"item_id": item_id, "item_name": item_name, "stock_count": stock_count, "price": price}

    def update_item(self, item_id, stock_count, price):
        if item_id in self.items:
            self.items[item_id]["stock_count"] = stock_count
            self.items[item_id]["price"] = price
        else:
            print("not found")

    def check_item_details(self, item_id):
        if item_id in self.items:
            print(
                f"{self.items[item_id]['item_name']}: {self.items[item_id]['stock_count']}: {self.items[item_id]['price']}")
        else:
            print("not found")


inv = Inventory()
inv.add_item(123, "Mango", 10, 20)
inv.update_item(123, 40, 50)
inv.check_item_details(123)

inv.check_item_details(1234)