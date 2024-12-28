import json

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    ALL_DATA = json.load(file)

# Now 'data' contains the contents of the JSON file as a Python dictionary or list

##############################
###  Function Definitions
##############################

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

playAgain = True

prompt("Choose either 'en' for English or 'fr' pour francais:")
language = input()
while language not in ["en", "fr"]:
    prompt("Invalid input. Please try again.")
    language = input()

# Set Language
MESSAGES = ALL_DATA[language]

while playAgain:
    print(MESSAGES["welcome"])

    # Ask the user for the first number.
    prompt(MESSAGES["first_number"])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES["invalid_number"])
        number1 = input()

    # Ask the user for the second number.
    prompt(MESSAGES["second_number"])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES["invalid_number"])
        number2 = input()

    print(f'{number1} {number2}')

    # Ask the user for an operation to perform.
    prompt(MESSAGES["choose_operator"])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(MESSAGES["invalid_operator"])
        operation = input()

    # Perform the operation on the two numbers.
    match operation:
        case '1':   # '1' represents addition
            output = int(number1) + int(number2)
        case '2': # '2' represents subtraction
            output = int(number1) - int(number2)
        case '3': # '3' represents multiplication
            output = int(number1) * int(number2)
        case '4': # '4' represents division
            output = int(number1) / int(number2)

    # Print the result to the terminal.
    print(f"{MESSAGES["display_output"]} {output}")

    # Ask to play again
    prompt(MESSAGES["play_again"])
    response = input()
    if (response in MESSAGES["play_again_responses"]):
        playAgain = True
    else:
        playAgain = False