# Dictionary = Grocery items & prices
# Menu function to allow users to select options to add items to a shopping cart
# Checkout option with cash or card payment
# Card payment method that checks for any valid 4 digit PIN

grocery_items = { # Dictionary (Item(key) : Price(value))
    "apple": 0.50,
    "banana": 0.30,
    "bread": 2.50,
    "milk": 3.50,
    "eggs": 3.30,
    "cheese": 2.75,
    "chicken": 5.20,
    "rice": 3.70,
    "pasta": 2.75,
    "tomato": 0.40
}

cart = [] # Empty list for user shopping cart

def store_menu(): # Function that displays menu options, will be called each time through main loop
    print("\nWelcome to the Grocery Store!")
    print("Please choose an option:")
    print("1. View items")
    print("2. Add item to cart")
    print("3. View cart")
    print("4. Checkout")
    print("5. Exit")

def display_items(): # Function to show all grocery items and their prices through the dictionary and prints each item in a format
    print("\nAvailable items:")
    for item, price in grocery_items.items(): # returns a list of key value pairs in the dictionary and storing them as item and price
        print(f"{item.title()}: ${price:.2f}") # Title case format for item

def add_to_cart(): # Function to allow user to add items to their cart
    display_items() # Displays available items
    print("\nType the name of the item to add to your cart.") # Displays instructions to the user
    print("Type 'done' when you are finished.")
    while True: # Continuous loop until broken
        item = input("Add item:").lower() # lowercases user input
        if item == "done":
            break # Loop can only break if user types 'done'
        elif item in grocery_items: # if item exists in dictionary
            cart.append(item) # add item to the cart list 
            print(f"{item.title()} added to cart.") # display a success message
        else:
            print("Item not found. Try again.") # If error 

def view_cart(): # Function to display what is in the user cart
    if not cart: # if cart is empty
        print("Your cart is empty.")
    else:
        print("\nItems in your cart:") # Display message
        total = 0
        for item in cart: # For each element in cart list
            price = grocery_items[item] # price of item inside of grocery dictionary
            total += price # update total to include new price each time
            print(f"{item.title()} - ${price:.2f}") # display price of item
        print(f"Total: ${total:.2f}") # display total once for-loop is done

def checkout(): # Function to handle payment
    if not cart: # If cart is empty
        print("Your cart is empty.")
        return
    
    total = sum(grocery_items[item] for item in cart) # sum of all values inside of cart list based on item keys
    print(f"\nYour total is: ${total:.2f}") 
    method = input("Payment Method: Cash / Card?: ").lower() # asks for payment then lowercases input
    if method == "cash": # if cash, successful
        print("Payment successful. Thank you for shopping!")
    elif method == "card": # if card, asks for 4 digit pin
        pin = input("Enter your 4-digit PIN: ")
        if pin.isdigit() and len(pin) == 4: # checks if PIN is alphanumeric and length is 4, print success
            print("Payment successful. Thank you for shopping!")
        else:
            print("Invalid PIN. Transaction failed.")
    else: # Handles input that isnt cash or card
        print("Invalid payment method.")

while True:
    store_menu() # Function that displays menu options, will be called each time through main loop
    choice = input("Enter your choice (1-5):")
    if choice == "1":
        display_items() # Function to show all grocery items and their prices through the dictionary and prints each item in a format
    elif choice == "2":
        add_to_cart() # Function to allow user to add items to their cart
    elif choice == "3":
        view_cart() # Function to display what is in the user's cart
    elif choice == "4":
        checkout() # Function to handle payment
        break 
    elif choice == "5": # Exit
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")



# Add quantity support (allow user to add multiple apples, update quantities in cart)
# Improve checkout flow (confirm cart contents, allow changing cart before payment)
# Error handling wihtout crashing
# Add persistence (Save/ load cart data to a text file)
# GUI with Tkinter or web app with flask
# Unit tests for functions
# README for project usage/ features
