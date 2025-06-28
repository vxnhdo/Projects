def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def division(a, b):
    if b == 0: # Input checking
        return "Error, cannot divide by zero."
    return a / b

operator = input("Enter an operator ( + - * /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = division(num1, num2)
else:
    print("Invalid operator.")
print("Result: ", result)
print("Thanks for using the calculator.")

# Input validation needed, loop support to allow multiple calculations without restarting the program, support more operators, better error handling, GUI, unit tests, command line flags