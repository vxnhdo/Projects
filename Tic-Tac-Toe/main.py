import random # Randomly choose word from list
import string
from words import words

def get_valid_word(words: list[str]): # pass in a list
    word = random.choice(words) # assign word to random.choice with words list as parameter
    while "-" in word or " " in word: # while a dash/ a white space is in a word, keep choosing that word
        word = random.choice(words)
    
    return word.upper() # Return the word once while loop is complete

def hangman():
    word = get_valid_word(words) # saves return value from function inside of word 
    word_letters = set(word) # saves all words as a set 
    alphabet = set(string.ascii_uppercase) # import a set of uppercase charaacters from dictionary
    used_letters = set() # keeps track of user guesses

    lives = 10

    while len(word_letters) > 0 and lives > 0: # get user input
        print(f"You have {lives} left and have used: ", ' '.join(used_letters)) # .join() turns iteratable into a string, seperated by a space

        word_list = [letter if letter in used_letters else "-" for letter in word] # shows current guess, seperated with dashes for letters they have not guessed
        print("Current word: ", " ".join(word_list))
        user_guess = input("Guess a letter: ").upper() 
        if user_guess in alphabet - used_letters: # if input is a valid char inside alphabet that hasn't been used yet...
            used_letters.add(user_guess) # add it to used_letters set
            if user_guess in word_letters: # if letter guessed is in the word...
                word_letters.remove(user_guess) # remove letter so it decreases in size

            else: # Takes away life for incorrect guess
                lives -=1
                print("Letter is not in word.")
 
        elif user_guess in used_letters:
            print("You have already used that character. Try again")
        else:
            print("Invalid character.")

        # gets here when len of word_letters == 0 OR when lives == 0
        if lives == 0:
            print(f"Sorry you died, the word was {word}.")
        else:
            print(f"You guessed correctly, the word is {word}.")

hangman()        

