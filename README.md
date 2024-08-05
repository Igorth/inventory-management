# Inventory Management System

This project is a simple command-line interface (CLI) for managing an inventory of items in a store. It allows users to add new items, update quantities, remove items, check stock, and list all items in the inventory. The project demonstrates the use of various Python data structures such as lists, sets, tuples, and dictionaries.

## Features

- **Add New Items**: Add new items to the inventory with a name, category, price, and quantity.
- **Update Quantity**: Update the quantity of existing items in the inventory.
- **Remove Items**: Remove items from the inventory.
- **Check Stock**: Check the stock quantity of a specific item.
- **List Items**: List all items in the inventory along with their details and display items that are low in stock.

## Data Structures Used

- **List**: To keep track of items that are low in stock.
- **Set**: To store unique item categories.
- **Tuple**: To store item details (name, category, price).
- **Dictionary**: To store the inventory with item names as keys and quantities as values.

## Getting Started

### Prerequisites

- I am using the Python version 3.12

### Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/inventory-management-system.git
   cd inventory-management-system
   ```

2. Run the program:
   ```sh
   python main.py
   ```

## Usage

Follow the on-screen instructions to interact with the Inventory Management System through the command-line interface.

### Example

```sh
Inventory Management System
1. Add item
2. Update quantity
3. Remove item
4. Check stock
5. List items
6. Exit
Enter your choice: 1

Enter item name: Laptop
Enter item category: Electronics
Enter item price: 1000
Enter item quantity: 10
Added Laptop to the inventory with quantity 10.

Enter your choice: 5
Current Inventory:
Item: Laptop, Category: Electronics, Price: $1000.0, Quantity: 10

Low Stock Items:

Enter your choice: 6
Exiting the Inventory Management System.
```

## Project Structure

```
inventory-management-system/
├── main.py
└── README.md
```
