import tkinter as tk
from PIL import Image, ImageTk

class FullScreenApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Loan Manager")
        self.attributes("-fullscreen", True)  # Set fullscreen attribute
        self.bind("<Escape>", self.quit_fullscreen)  # Bind Escape key to exit fullscreen
        self.configure(background="blue")

        # Set the window icon
        icon_path = r"C:\Users\smahd\OneDrive\Desktop\pyloan\loan_app\resources\Loan_icon.jpeg"
        img = Image.open(icon_path)
        self.iconphoto(False, ImageTk.PhotoImage(img))

        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        # Create menu items
        self.dashboard_menu = tk.Menu(self.menu, tearoff=0)
        self.dashboard_menu.add_command(label="Dashboard", command=self.display_dashboard)
        self.dashboard_menu.add_command(label="New Loan", command=self.add_new_loan)
        self.dashboard_menu.add_command(label="Current Loans", command=self.display_current_loans)
        self.menu.add_cascade(label="Menu", menu=self.dashboard_menu)

        # Display dashboard by default
        self.display_dashboard()

    def display_dashboard(self):
        # Implement the dashboard display
        # Create a frame to display loan details and charts
        dashboard_frame = tk.Frame(self)
        dashboard_frame.pack(fill=tk.BOTH, expand=True)
        # Add loan details table, charts, and interactivity
        # ... (code for dashboard layout)

    def add_new_loan(self):
        new_loan_window = NewLoanWindow()
       # new_loan_window = tk.Toplevel()  # Create a Toplevel window
        new_loan_window.mainloop()

    def display_current_loans(self):
        # Functionality to display current loans
        pass

    def quit_fullscreen(self, event):
        self.attributes("-fullscreen", False)  # Exit fullscreen

class NewLoanWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("New Loan")
        self.geometry("400x300")  # Adjust the window size as needed
        self.configure(background="white")  # Set the background color
        
        # Creating widgets for entering loan details
        tk.Label(self, text="Starting Date").pack()
        self.starting_date_entry = tk.Entry(self)
        self.starting_date_entry.pack()

        tk.Label(self, text="Principal Amount").pack()
        self.principal_amount_entry = tk.Entry(self)
        self.principal_amount_entry.pack()

        tk.Label(self, text="Annual Interest").pack()
        self.annual_interest_entry = tk.Entry(self)
        self.annual_interest_entry.pack()

        tk.Label(self, text="Number of Payments").pack()
        self.num_payments_entry = tk.Entry(self)
        self.num_payments_entry.pack()

        # Radio buttons for payment frequency
        self.payment_frequency = tk.StringVar(value="Annual")  # Default value
        tk.Radiobutton(self, text="Annual", variable=self.payment_frequency, value="Annual").pack()
        tk.Radiobutton(self, text="Monthly", variable=self.payment_frequency, value="Monthly").pack()
        tk.Radiobutton(self, text="Weekly", variable=self.payment_frequency, value="Weekly").pack()
        tk.Radiobutton(self, text="Daily", variable=self.payment_frequency, value="Daily").pack()

        # Button to calculate and display loan details
        tk.Button(self, text="Calculate Loan", command=self.calculate_loan).pack()

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
    app = FullScreenApp()
    app.mainloop()

if __name__ == "__main__":
    main()
