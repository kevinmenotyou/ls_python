import json

# Open the JSON file for reading
with open('mortgage_calculator_messages.json', 'r') as file:
    DATA = json.load(file)

# Decide what input formats your program expects. For example, should the user enter an interest rate of 5% as 5 or .05?
# If you're working with an Annual Percentage Rate (APR), you need to convert it to a monthly interest rate for use in the formula.
# Be careful about the loan duration -- are you working with months or years? Choose variable names carefully to assist in remembering.
# Think about edge cases. There are plenty of edge cases to work with in this problem, and each presents interesting challenges. 
# For instance, consider whether you want to support no-interest loans or loans that might be payable over a period of time
# that is not an integer number of years (for instance, 2.5 years (30 months)). 

# Inputs
# - the loan amount
# - the Annual Percentage Rate (APR)
# - the loan duration
# Outputs
# - monthly payment to 2 decimal places
# - loan duration in months
# Examples
# - Only numbers are input
# - Non numbers are inputed
# - 0 is inputted (divided)

MONTHS_IN_YEAR = 12

def get_loan_duration_months(loan_duration_years):
    return loan_duration_years * MONTHS_IN_YEAR

def get_monthly_interest_rate(annual_percentage_rate):
    return annual_percentage_rate / MONTHS_IN_YEAR

def get_monthly_payment(loan_amount, monthly_interest_rate, loan_duration_months):
    return loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-loan_duration_months)))

def is_valid_numeric_input(input):
    try:
        number = float(input)
        if (number > 0)
        return True
    except:
        print("Input was invalid. Please enter a valid number greater than 0.")
        return False

def get_valid_numeric_input():
    my_input = input("==> ")
    if (is_valid_numeric_input(my_input)):
        return float(my_input)
    else:
        return get_valid_numeric_input()

print(DATA["welcome_message"])

while (True):
    print(DATA["loan_question"])
    loan_amount = get_valid_numeric_input()

    print(DATA["annual_rate_question"])
    annual_interest_rate = get_valid_numeric_input() / 100
    monthly_interest_rate = get_monthly_interest_rate(annual_interest_rate)

    print (DATA["loan_duration_question"])
    loan_duration_years = get_valid_numeric_input()
    loan_duration_months = get_loan_duration_months(loan_duration_years)
    print (f"{DATA["print_loan_duration_result"]} {loan_duration_months}")

    monthly_payment = get_monthly_payment(loan_amount, monthly_interest_rate, loan_duration_months)
    print (f"{DATA["print_monthly_payment_result"]} {round(monthly_payment, 2)}")

    print (DATA["calculate_again_question"])
    answer = input()

    if answer not in DATA["valid_play_again_answers"]:
        break