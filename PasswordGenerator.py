import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    # Define possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    # Initialize the string containing all possible characters
    characters = letters

    # Add digits if the option is enabled
    if numbers:
        characters += digits

    # Add special characters if the option is enabled
    if special_characters:
        characters += specials

    # Initialize the generated password and security criteria flags
    password = ""
    meets_criteria = False
    has_number = False
    has_specials = False

    # Generate the password until all criteria are met
    while not meets_criteria or len(password) < min_length:
        # Select a random character from the allowed characters
        new_char = random.choice(characters)
        password += new_char

        # Check if the new character is a digit or special character
        if new_char in digits:
            has_number = True
        elif new_char in specials:
            has_specials = True

        # All criteria are met only if numbers and special characters are present, if needed
        meets_criteria = True
        if numbers:
            meets_criteria = meets_criteria and has_number
        if special_characters:
            meets_criteria = meets_criteria and has_specials

    return password

def get_yes_no_input(message):
    # Function to get a 'yes' or 'no' response from the user
    while True:
        user_input = input(message).lower()
        if user_input == 'y' or user_input == 'n':
            return user_input
        else:
            print("Incorrect input. Please enter 'y' for 'Yes' or 'n' for 'No'.")

# Prompt for the minimum password length and options for numbers and special characters
min_length = int(input("Enter the minimum length: "))
has_number = get_yes_no_input("Do you want to have numbers? (y/n): ") == "y"
has_specials = get_yes_no_input("Do you want to have special characters? (y/n): ") == "y"

# Generate the password and display the result
pwd = generate_password(min_length, has_number, has_specials)
print("The generated password is:", pwd)
