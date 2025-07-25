"""
MAIN Program Logic
1. Take a DAILY MESSAGE from User
2. Ask for a tag to associate the note
3. APPEND the messsage to 'daily_notes.txt'
4. Include the current DATE & TIME & TAG with each note
"""
from datetime import datetime
from colorama import Fore, Style


# Function to run when user selects option 1 (Add a New Note)
def add_new_note():
    while True:
        # Ask for the user's note
        note = input("Begin typing your note (or 'EXIT' to Quit): ")

        # Exit handling
        if note.lower() == 'exit':
            print("Exiting to menu...")
            break

        # Ask the user for a tag to sort their note by
        tag = input("Enter a tag for this note (e.g. Work, Personal, Health...): ")

        # Get the date/time for the current entry
        timestamp = datetime.now().astimezone().strftime("[%m/%d/%Y - %I:%M %p]")

        # Create a formatted message to be appended to the text file
        formatted_msg = f"{timestamp} - {Fore.BLUE}{tag}{Style.RESET_ALL} - {note}"

        # Append the formatted message to the text file
        with open("daily_notes.txt", "a") as file:
            file.write(formatted_msg + "\n")

        # Confirmation message
        print(Fore.GREEN + "Note saved." + Style.RESET_ALL)


# Function to run when user selects option 2 (View Recent Notes)
def view_recent_notes():
    try:
        with open("daily_notes.txt", "r") as file:
            # Open file in and read the most recent 5 files 
            notes = file.readlines()[-5:]
            print("--- Recent Notes ---\n")
            for note in notes:
                print(note.strip()) 
            print()
    except FileNotFoundError:
        print(Fore.YELLOW + "Notes not found, Begin by writing one." + Style.RESET_ALL)


# Function to run when a user selects option 3 (Search for a Note)
def search_notes():
    # Ask for input to search for
    target = input("Enter tag / keyword to search for: ").lower()
    # Set a boolean flag to change if found
    isFound = False

    try:
        with open("daily_notes.txt", "r") as file:
            # Iterate through each line in the file and if the target is in the line, display it and set boolean flag to True
            for line in file:
                if target in line.lower():
                    print(line.strip())
                    isFound = True

    # If file opening fails, print error message and return nothing
    except FileNotFoundError:
        print("No notes found, file does NOT exist.")
        return 

    if not isFound:
        print(f"No keyword / tag found matching: {target}")


# Write main program logic, we want the menu to run until the user wants to quit
while True:
    print(Fore.GREEN + "Daily Note Logger Menu" + Style.RESET_ALL)
    print("1. Add a New Note")
    print("2. View Recent Notes")
    print("3. Search for a Note")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add a New Note
    if choice == 1:
        add_new_note()
    elif choice == 2:
        view_recent_notes()
    elif choice == 3:
        search_notes()
    elif choice == 4:
        print("Exiting program...")
        break
    else:
        print(Fore.RED + "Error, invalid choice must be 1, 2, or 3." + Style.RESET_ALL)