# Make madlibs more dynamic by placing random words using placeholders in each story
# Randomly shuffle where inputs appear
# Insert words in different places each time
# Randomized story features, same input appears in different places each time

import random
import time
print("Welcome to Random Mad Libs!\n")
print("Enter the following words...")
time.sleep(1)

# Collect user input for story templates inside of a dictionary to hold key-value pairs
inputs = {
    "name": input("Enter your name: "),
    "place": input("Enter a place: "),
    "adj1": input("Enter an adjective: "),
    "adj2": input("Enter another adjective:"),
    "noun1": input("Enter a noun: "),
    "noun2": input("Enter another noun: "),
    "verb1": input("Enter a verb: "),
    "verb2": input("Enter another verb: "),
    "animal": input("Enter an animal: "),
    "food": input("Enter your favorite food: "),
    "emotion": input("Enter an emotion: ")
}

# Define story templates with placeholders for each key inside of 'inputs' dictionary using a List
stories = [
    """Today, {name} visited the {adj1} {place}.
    They saw a {animal} bouncing a {noun1} while trying to {verb1}.
    Later, they went and purchased {food} and felt {emotion} while shopping.
    It was a {adj2} day. especially when the {noun2} started to {verb2}.""", # Story 1

    """Once upon a time, {name} found a magical {noun1} in the {place}.
    It was guarded by a {adj1} {animal} who refused to let anyone {verb1}.
    In order to distract it, {name} offered {food} and danced {verb2}-fully.
    The {animal} smiled and said, "You're the most {emotion} person I have ever met!
    Then the {animal} disappeareed into a puff of {adj2} smoke, leaving behind a {noun2}.""", # Story 2

    """In the far-off land of {place}, lived a {adj1} creature named {name}.
    Every morning, they {verb1} with their pet {animal}, who loved eating {food}.
    One day, a {noun1} fell from the sky, making everyone feel {emotion}.
    The whole village had to {verb2} until {adj2} {noun2} saved the day.""" # Story 3
]

# Randomly choose a template using random.choice() method
rand_story = random.choice(stories)

# Fill in placeholders with user input by using .format() method
final_story = rand_story.format(**inputs)

# Display the random story
print("\nHere is your MadLib story...")
print(final_story)