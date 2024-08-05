class Inventory:
    def __init__(self):
        self.inventory = {}  # Dictionary to store item_name: quantity
        self.categories = set()  # Set to store unique items categories
        self.low_stock_items = []  # List to store items with low stock
        self.item_details = {}  # Dictionary to store item_name: (category, price)

    def add_item(self, item_name, category, price, quantity):
        if item_name in self.inventory:
            print(f"{item_name} already exists in the inventory. Use Update to change the quantity.")
        else:
            self.inventory[item_name] = quantity
            self.categories.add(category)
            self.item_details[item_name] = (category, price)
            print(f"Added {item_name} to the inventory with quantity {quantity}.")

    def update_quantity(self, item_name, quantity):
        if item_name in self.inventory:
            self.inventory[item_name] += quantity
            print(f"Updated {item_name} quantity to {self.inventory[item_name]}")
            if self.inventory[item_name] <= 5:
                if item_name not in self.low_stock_items:
                    self.low_stock_items.append(item_name)
                    print(f"{item_name} is now low in stock.")
            else:
                if item_name in self.low_stock_items:
                    self.low_stock_items.remove(item_name)
        else:
            print(f"{item_name} does not exist in the inventory. Add an item to the inventory first.")

    def remove_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]
            del self.item_details[item_name]
            if item_name in self.low_stock_items:
                self.low_stock_items.remove(item_name)
            print(f"Removed {item_name} from the inventory.")
        else:
            print(f"{item_name} does not exist in the inventory.")

    def check_stock(self, item_name):
        if item_name in self.inventory:
            quantity = self.inventory[item_name]
            print(f"{item_name} has {quantity} units in stock.")
            return quantity
        else:
            print(f"{item_name} does not exist in the inventory.")
            return None

    def list_items(self):
        print("Current Inventory:")
        for item_name, quantity in self.inventory.items():
            category, price = self.item_details[item_name]
            print(f"Item {item_name}, Category: {category}, Price: ${price}, Quantity: {quantity} ")
        print("\nLow Stock Items:")
        for item in self.low_stock_items:
            print(f"Item {item}, Quantity: {self.inventory[item]}")


def main():
    store_inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add item")
        print("2. Update quantity")
        print("3. Remove item")
        print("4. Check stock")
        print("5. List items")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item_name = input("Enter item name: ")
            category = input("Enter item category: ")
            price = float(input("Enter item price: "))
            quantity = int(input("Enter item quantity: "))
            store_inventory.add_item(item_name, category, price, quantity)

        elif choice == "2":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            store_inventory.update_quantity(item_name, quantity)

        elif choice == "3":
            item_name = input("Enter item name: ")
            store_inventory.remove_item(item_name)

        elif choice == "4":
            item_name = input("Enter item name: ")
            store_inventory.check_stock(item_name)

        elif choice == "5":
            store_inventory.list_items()

        elif choice == "6":
            print(f"Exiting the Inventory Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
