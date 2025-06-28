principle = 0 # Contains amount owed
rate = 0 # Interest Rate
time = 0 # Duration in years

while True: # Loop to ask for input for principle
    principle = float(input("Enter the principle amount: $"))
    if principle < 0:
        print("Principle cannot be less than zero.")
    else:
        break

while True: # Loop to ask for input for rate
    rate = float(input("Enter the interest amount: %"))
    if rate < 0:
        print("Interest rate cannot be less than zero.")
    else:
        break

while True: # Loop to ask for input for time
    time = float(input("Enter the time IN YEARS: "))
    if time < 0:
        print("Time cannot be less than zero.")
    else:
        break

print(f"${principle:,.2f} dollars.")
print(f"% {rate:.2f} interest rate.")
print(f"Duration: {time} years.")

total = principle * pow((1 + rate/100), time) # Interest rate equation

print(f"Balance after {time} years is: ${total:,.2f}.")


# Wrap logic into functions, add input error hjandling with try/ except blocks to catch non-numeric input, support simple interest as an option alongside compound interest, add ability to enter interest compounding frequency(monthly, quarterly, bi-year, yearly), include unit tests for calculation functions, README, make it interactive with options to do multiple calculations wihtout restarting