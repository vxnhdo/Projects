# TASK: Create a ticket pricing system based on age & membership

# Ticket price function = takes integer "age" and bool "is_member"
def ticket_price(age, is_member):
    price = (
        5 if age <= 12 else # $5 if age is less than or equal to 12
        8 if age <= 17 else  # $8 if age is less than or equal to 17
        12 if age <= 64 else  # $12 if age is less than or equal to 64
        7 # else, price is $7
    )

    discount = 0.2 if is_member else 0 # 20% discount if a member
    final_price = price * (1 - discount) # final price = price X discount

    # "Budget" if final_price is less than $8, else "Standard" if final_price is less than or equal to 10 else "Premium"
    label = "Budget" if final_price < 8 else "Standard" if final_price <= 10 else "Premium"


    return final_price, label

age = int(input("Enter age: "))
is_member = input("Are you a member? (yes/no): ").strip().lower() # Remove whitespace & lowercase input
is_member = True if is_member == "yes" else False

price, label = ticket_price(age, is_member)

print(f"\nYour ticket price is: {price:,.2f} ({label}) ticket.")


# Add input validation to handle invalid ages or membership inputs, add support for more membership types or seasonal pricing, extend with a menu or CLI to buy multiple tickets or process a group, add unit tests to vcerify pricing and labels, package as a module or a larger event booking app, provide a README for pricing rules & usage
