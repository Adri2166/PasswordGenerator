import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += specials

    password = ""
    meets_criteria = False
    has_number = False
    has_specials = False

    while not meets_criteria or len(password) < min_length:
        new_char = random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number = True
        elif new_char in specials:
            has_specials = True

        meets_criteria = True

        if numbers:
            meets_criteria = meets_criteria and has_number
        if special_characters:
            meets_criteria = meets_criteria and has_specials

    return password

def get_yes_no_input(message):
    while True:
        user_input = input(message).lower()
        if user_input == 'y' or user_input == 'n':
            return user_input
        else:
            print("Incorrect input. Please enter 'y' for 'Yes' or 'n' for 'No'.")

min_length = int(input("Enter the minimum length: "))
has_number = get_yes_no_input("Do you want to have numbers? (y/n): ") == "y"
has_specials = get_yes_no_input("Do you want to have special characters? (y/n): ") == "y"
pwd = generate_password(min_length, has_number, has_specials)

print("The generated password is:", pwd)
