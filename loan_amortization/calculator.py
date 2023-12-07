# Pyloan
# calculator.py

def calculate_amortization(principal, annual_interest_rate, years):
    r = annual_interest_rate / 100 / 12  # Monthly interest rate
    n = years * 12  # Total number of payments

    # Calculate monthly payment
    monthly_payment = (principal * r) / (1 - (1 + r) ** -n)

    # Generate amortization schedule
    balance = principal
    amortization_schedule = []
    for i in range(1, n + 1):
        interest = balance * r
        principal_payment = monthly_payment - interest
        balance -= principal_payment
        amortization_schedule.append({
            "Month": i,
            "Balance": round(balance, 2),
            "Principal": round(principal_payment, 2),
            "Interest": round(interest, 2)
        })

    return {
        "MonthlyPayment": round(monthly_payment, 2),
        "AmortizationSchedule": amortization_schedule
    }
