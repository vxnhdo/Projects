import random 

def guess(x: int):
    random_num = random.randint(1, x) # Return a random integer between 1 and x
    guess = 0 # define guess so it can be changed later

    while (guess != random_num): # while condition is not true, iterate the following code block...
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_num:
            print("Too low!")
        elif guess > random_num:
            print("Too high!")

    print(f"Congrats! The correct answer was {random_num}!") # if guess = random_num, while loop won't run and will print this line

# Computer will have to try and guess a number WE choose

def computer_guess(x: int):
    # Set low & high values
    low = 1
    high = x
    feedback = ""  # Initialize feedback w/ empty string so there's no guess

    while feedback != 'c': # c = correct, while feedback is not correct
        if low != high:
            guess = random.randint(low, high) # guess = random integer between 1 and x
        else: 
            guess = low
        
        feedback = input(f"Is {guess} too high (H), too low (L) or correct (C)?: ").lower() # Takes input and lowercases all characters

        if feedback == 'h': # If feedback is too high, adjust our upperbound
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        
    print(f"Correct guess = {guess}!") # Correct answer feedback outside of while loop


computer_guess(100)
