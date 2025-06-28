# Use Variables, Typecasting and User input
# Ask the user for their income and expense, then calculate how much money they have at the end of the month

# Ask for Income
income = float(input("Enter your monthly income: $"))

# Ask for Expenses (Rent, Groceries, Transport and Utilities)
rent = float(input("Enter your monthly rent: $"))
groceries = float(input("Enter your monthly grocery spending: $"))
transport = float(input("Enter your transportation costs: $"))
utilities = float(input("Enter your monthly utilities: $"))

expense_total = rent + groceries + transport + utilities
savings = income - expense_total

# Display results
print(f"Monthly Income: ${income:.2f}")
print(f"Monthly Expenses: ${expense_total:.2f}")
print(f"Total Savings: ${savings:.2f}")

# Display a message based on savings
if savings > 0:
    print("Saving this month.")
elif savings == 0:
    print("Breaking even this month.")
else:
    print("Overspent this month.")

# Input validation, allow user to enter variable numbers of expense categories dynamically, add monthly summaries or projections, wrap code into functions, build a GUI or web interface for interaction, add file export/ import (save/ load budgets), include visualization (charts) of expenses vs income, provide README