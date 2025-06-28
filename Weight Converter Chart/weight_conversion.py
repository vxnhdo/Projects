weight = float(input("Enter weight: "))
unit = input("Kilograms or Pounds? (K/L): ")
if unit == "K" or unit == "k":
    weight *= 2.205
    print(f"Your weight in pounds is: {weight:.2f} lbs.")
elif unit=="L" or unit=="l":
    weight /= 2.205
    print(f"Your weight in kilograms in: {weight:.2f} kgs.")
else:
    print(f"{unit} is NOT allowed.")

# 1. Add input validation
# 2. Support more units (grams, ounces)
# 3. Build a GUI so its more user friendly\
# 4. Package it so its a reuseable module/ script with functions
# 5. Add unit tests (show you know how to test your code)
# 6. Add comments & README