# P
# Input 6 Numbers
# Output whether 6th number exists in 5 numbers
# Text is number?
# E
"""
Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 17

17 is in 25,15,20,17,23.

Enter the 1st number: 25
Enter the 2nd number: 15
Enter the 3rd number: 20
Enter the 4th number: 17
Enter the 5th number: 23
Enter the last number: 18

18 isn't in 25,15,20,17,23.
"""

# D
# fun: Prompt for Number
# fun: Find number in Array
# fun: print ordinal ending

# A
# loop 5 times
# - prompt for number
# - validate input
# - store number in array
# prompt 6th time
# compare 6th number
# check result
# return result

# C

ORDINAL = {
    "1": "1st",
    "2": "2nd",
    "3": "3rd",
    "4": "4th",
    "5": "5th",
    "6": "6th",
}

def prompt(string):
    print (f"### {string}")

def prompt_for_number(number):
    prompt(f"Enter the {print_ordinal(number)} number:")
    try:
        my_number = int(input())
        return str(my_number)
    except:
        prompt("Input not valid! Expecting an integer.")
        return prompt_for_number(number)

def print_ordinal(number):
    return ORDINAL[f"{number}"]

def __main__():

    my_numbers = []

    for i in range(1,6):
        my_number = prompt_for_number(i)
        my_numbers.append(my_number)
    sixth_number = prompt_for_number(6)

    if (sixth_number in my_numbers):
        print(f"{sixth_number} is in {",".join(my_numbers)}.")
    else:
        print(f"{sixth_number} is not in {",".join(my_numbers)}.")

__main__()


    