# calculator.py
import pandas as pd

def calculate_amortization(principal, annual_interest_rate, years):
    r = annual_interest_rate / 100 / 12  # Monthly interest rate
    n = years * 12  # Total number of payments

    # Calculate monthly payment
    monthly_payment = (principal * r) / (1 - (1 + r) ** -n)

    # Generate amortization schedule
    balance = principal
    periods = []
    for i in range(1, n + 1):
        interest = balance * r
        principal_payment = monthly_payment - interest
        balance -= principal_payment
        periods.append([i, round(monthly_payment, 2), round(interest, 2), round(principal_payment, 2), round(balance, 2)])

    # Create a DataFrame using Pandas
    columns = ["Period", "Monthly Payment", "Interest", "Principal", "Balance"]
    amortization_table = pd.DataFrame(periods, columns=columns)

    # Return a dictionary containing the AmortizationTable key
    return {
        "MonthlyPayment": round(monthly_payment, 2),
        "AmortizationTable": amortization_table.to_dict('records')  # Convert DataFrame to a list of dictionaries
    }
