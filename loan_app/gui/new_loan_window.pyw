import tkinter as tk

class NewLoanWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("New Loan")
        self.geometry("400x300")  # Set the window size explicitly
        self.configure(background="white")  # Set the background color

        fields = [
            ("Starting Date", tk.Entry),
            ("Principal Amount", tk.Entry),
            ("Annual Interest", tk.Entry),
            ("Number of Payments", tk.Entry)
        ]

        for label_text, widget_type in fields:
            frame = tk.Frame(self, bg='white')
            frame.pack(fill=tk.X)
            label = tk.Label(frame, text=label_text, bg='white', width=15, anchor='w')
            label.pack(side=tk.LEFT, padx=10, pady=5)
            entry = widget_type(frame)
            entry.pack(fill=tk.X, padx=10, expand=True)

def main():
    new_loan_window = NewLoanWindow()
    new_loan_window.mainloop()

if __name__ == "__main__":
    main()
