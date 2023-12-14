import tkinter as tk

class NewLoanWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("New Loan")
        self.geometry("400x300")  # Set the window size explicitly
        self.configure(background="white")  # Set the background color

        fields = [
            "Starting Date",
            "Principal Amount",
            "Annual Interest",
            "Number of Payments"
        ]

        for idx, label_text in enumerate(fields):
            label = tk.Label(self, text=label_text, bg='white')
            label.grid(row=idx, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(self)
            entry.grid(row=idx, column=1, padx=10, pady=5, sticky="ew")

def main():
    new_loan_window = NewLoanWindow()
    new_loan_window.mainloop()

if __name__ == "__main__":
    main()
