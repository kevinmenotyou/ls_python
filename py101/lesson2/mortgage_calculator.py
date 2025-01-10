import json

# Open the JSON file for reading
with open('mortgage_calculator_messages.json', 'r') as file:
    DATA = json.load(file)

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

def get_loan_duration_months(loan_in_years):
    return loan_in_years * MONTHS_IN_YEAR

def get_monthly_interest_rate(annual_rate):
    return annual_rate / MONTHS_IN_YEAR

def get_monthly_payment(
        amount,
        rate,
        loan_duration
    ):
    return amount * (rate / (1 - (1 + rate) ** (-loan_duration)))

def is_valid_numeric_input(my_input):
    try:
        number = float(my_input)
        if (number <= 0):
            print(DATA["error_handling_0"])
            return False
        return True
    except ValueError:
        print(DATA["error_handling_invalid_number"])
        return False

def get_valid_numeric_input():
    my_input = input("==> ")
    if (is_valid_numeric_input(my_input)):
        return float(my_input)
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

    monthly_payment = get_monthly_payment(
        loan_amount, monthly_interest_rate, loan_duration_months)
    rounded_amount = round(monthly_payment, 2)
    print (f"{DATA["print_monthly_payment_result"]} {rounded_amount}")

    print (DATA["calculate_again_question"])
    answer = input()

    if answer not in DATA["valid_play_again_answers"]:
        break