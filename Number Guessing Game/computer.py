import random # Calls random function package, so we can call methods

def guess(x: int):
    random_num = random.randint(1, x) # Return a random integer between 1 and x
    guess = 0 # define guess so it exists & can be changed later

    # Create a While-loop 
    while (guess != random_num): # while guess is not equal to random_num, iterate
        guess = int(input(f"Guess a number between 1 and {x}: ")) # asks for guess
        if guess < random_num:
            print("Too low!")
        elif guess > random_num:
            print("Too high!")

    print(f"Congrats! The correct answer was {random_num}!") # if guess = random_num, while loop won't run and will print this line

guess(10) # Call function and place integer value for guess-range

# We are guessing the computer's number
    