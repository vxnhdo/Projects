# TASK: Ask for user's full name then display the first & last name using string indexing, # of characters, uppercase & lowercase versions, whether the name contains numbers, reversed name using slicing

name = input("Enter your full name: ").strip() # removes trailing/ leading whitespace

if " " not in name: # if whitespace is not in name
    print("Enter your first AND last name.")
else:
    space_index = name.index(" ") # find first white space
    first = name[:space_index] # first name = before 1st white space
    last = name[space_index + 1:] # last name = index after 1st white space till the end 

    print(f"First Name: {first}.")
    print(f"Last Name: {last}.")

    print(f"Full name uppercased: {name.upper()}.")
    print(f"Full name lowercased: {name.lower()}.")
    print(f"Full name reversed: {name[::-1]}.")
    print(f"Full name length: {len(name.replace(' ', ' '))}.") # replace spaces with nothing to count only characters

    if any(char.isdigit() for char in name): # if any character is True for isdigit() in each char in name, do this
        print("Name contains numbers.")
    else:
        print("Name only contains letters.")

# Allow multiple spaces in names, input validation to reject empty or numeric only names, providfe detailed analysis (word count, vowels, initials, constants, special characters), package into a function or class for reuse, Build a small app that processes multiple names (list or file input), add unit tests for functions