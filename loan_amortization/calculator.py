# calculator.py

import pandas as pd
pd.set_option('display.float_format', lambda x: '%.2f' % x)
def calculate_amortization(principal, annual_interest_rate, years):
    r = annual_interest_rate / 100 / 12  # Monthly interest rate
    n = years * 12  # Total number of payments

    # Calculate monthly payment
    monthly_payment = (principal * r) / (1 - (1 + r) ** -n)

    # Initialize lists for each column
    periods = list(range(1, n + 1))
    interest_list = []
    principal_list = []
    balance_list = []

    # Generate amortization schedule
    balance = principal
    for i in range(1, n + 1):
        interest = balance * r
        principal_payment = monthly_payment - interest
        balance -= principal_payment
        interest_list.append(interest)
        principal_list.append(principal_payment)
        balance_list.append(balance)

    # Create a DataFrame from the lists
    amortization_df = pd.DataFrame({
        'Period': periods,
        'Monthly Payment': monthly_payment,
        'Interest': interest_list,
        'Principal': principal_list,
        'Balance': balance_list
    })

    return amortization_df
