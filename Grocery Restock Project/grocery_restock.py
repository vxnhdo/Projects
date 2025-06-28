# Lists = Store employee names 
# Tuples = Product Information (price, quantity)
# Sets = Track unique items restocked
# Nested Loops

# List = Employee names
team = ["Greggory", "Bobbery", "Joshua"]

# Tuple = Product Name: (Price per unit, Quantity in stock)
products  = {
    "Apple": (0.5, 50),
    "Banana": (0.30, 30),
    "Carrot": (0.20, 40),
    "Watermelon": (5.0, 20),
    "Egg":(0.1, 100)
}

# Dictionary = Track items restocked by each employee
restocked_items = {
    "Greggory": set(),
    "Bobbery": set(),
    "Joshua": set()
}

product_list = list(products.keys()) # Creates a list of products for indexing based on the keys of the tuple

 # Simulate restocking for 3 days
for day in range(1,4):
    print(f"\nDay {day} restocking.")

     # Each employee will perform restocking on each day
    for employee in team:
        print(f"\n{employee} is restocking.")

        # Restocks 2 products per day
        for i in range(2): 
            # index = sum of day + restocking round number + length of employee name % length of product_list
            index = (day + i + len(employee)) % len(product_list) 

             # product = item at index of product_list
            product = product_list[index]

             # price & quantity = product inside of products dictionary
            price, quantity = products[product]

             # restocked_items at employee name will add the current product to record the employee stocked that one
            restocked_items[employee].add(product)

             # products at product = tuple of price with quantity plus 10
            products[product] = (price, quantity + 10)

            # show 10 units of product was restocked along with the new quantity
            print(f"Restocked 10 units of {product} (New quantity: {products[product][1]})") 

print("\nFinal Inventory")
# For each product in products dictionary, unpack the price & quantity then print the product name, quantity and price formated
for product, (price, quantity) in products.items():
    print(f"{product}: {quantity} units at ${price:.2f} each.")

print("\nRestocking Summary")
# For each employee in restocked_items, print their name followed by a comma-serpated list of all the products restocked
for employee, items in restocked_items.items():
    print(f"{employee} restocked: {', '.join(items)}.")

#  Add input validation, simulate dynamic restocking quantites (not always 10), add error handling (product not found, or quantity limits), refactor code into functions/ classes, expand features like tracking total inventory or daily restocking report, add unit test for key functions/ logic parts, README, add user interaction to allow manual restocknig or queries