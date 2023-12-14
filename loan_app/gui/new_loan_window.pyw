import tkinter as tk

class NewLoanWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("New Loan")
        self.geometry("400x300")  # Adjust the window size as needed
        self.configure(background="white")  # Set the background color

        self.create_loan_widgets()

    def create_loan_widgets(self):
        fields = [
            ("Starting Date", tk.Entry),
            ("Principal Amount", tk.Entry),
            ("Annual Interest", tk.Entry),
            ("Number of Payments", tk.Entry)
        ]

        for label_text, widget_type in fields:
            label = tk.Label(self, text=label_text)
            label.pack(anchor='w', padx=10, pady=5)
            entry = widget_type(self)
            entry.pack(anchor='w', padx=10, pady=5)

def main():
    new_loan_window = NewLoanWindow()
    new_loan_window.mainloop()

if __name__ == "__main__":
    main()
