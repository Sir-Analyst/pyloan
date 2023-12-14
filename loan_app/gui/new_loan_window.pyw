import tkinter as tk

class NewLoanWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("New Loan")
        self.geometry("800x500")  # Adjust the window size as needed
        self.configure(background="Blue")  # Set the background color
        
        # Creating widgets for entering loan details
        tk.Label(self, text="Starting Date").pack(anchor='w')
        self.starting_date_entry = tk.Entry(self)
        self.starting_date_entry.pack(anchor='w')

        tk.Label(self, text="Principal Amount").pack(anchor='w')
        self.principal_amount_entry = tk.Entry(self)
        self.principal_amount_entry.pack(anchor='w')

        tk.Label(self, text="Annual Interest").pack(anchor='w')
        self.annual_interest_entry = tk.Entry(self)
        self.annual_interest_entry.pack(anchor='w')

        tk.Label(self, text="Number of Payments").pack(anchor='w')
        self.num_payments_entry = tk.Entry(self)
        self.num_payments_entry.pack(anchor='w')

        # Radio buttons for payment frequency
        self.payment_frequency = tk.StringVar(value="Annual")  # Default value
        tk.Radiobutton(self, text="Annual", variable=self.payment_frequency, value="Annual").pack(anchor='w')
        tk.Radiobutton(self, text="Monthly", variable=self.payment_frequency, value="Monthly").pack(anchor='w')
        tk.Radiobutton(self, text="Weekly", variable=self.payment_frequency, value="Weekly").pack(anchor='w')
        tk.Radiobutton(self, text="Daily", variable=self.payment_frequency, value="Daily").pack(anchor='w')

        # Button to calculate and display loan details
        tk.Button(self, text="Calculate Loan", command=self.calculate_loan).pack(anchor='w')

    def calculate_loan(self):
        # Get the entered loan details and perform necessary calculations
        starting_date = self.starting_date_entry.get()
        principal_amount = float(self.principal_amount_entry.get())
        annual_interest = float(self.annual_interest_entry.get())
        num_payments = int(self.num_payments_entry.get())
        payment_frequency = self.payment_frequency.get()

        # Perform calculations and display total payment, total interest, etc.
        # ...

def main():
    new_loan_window = NewLoanWindow()
    new_loan_window.mainloop()

if __name__ == "__main__":
    main()
