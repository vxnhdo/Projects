unit = input("Celcius or Fahrenheit (C / F)?: ")
temp = float(input("Enter the temperature: "))

if unit == 'C' or unit == 'c':
    celcius_to_degrees = round(9 * temp / 5 + 32, 1) # Celcius to Fahrenheit equation
    print(f"Temperature in Fahrenheit = {celcius_to_degrees} degrees.")
elif unit == 'F' or unit == 'f':
    degree_to_celcius = round((temp - 32) * 5 / 9, 1) # Degree to Celcius equation
    print(f"Temperature in Celcius = {degree_to_celcius}")
else:
    print(f"{unit} was invalid.")

# Add input validation, make it case-insensitive/ more flexible, build a function/ class for reuseability, add a GUI or web interface, Add support for kelvin or other units, add unit tests, allowed repeated conversions in one loop (loop until user wants to exit)