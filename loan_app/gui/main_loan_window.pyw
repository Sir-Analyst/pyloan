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
        # Functionality to add a new loan
        pass

    def display_current_loans(self):
        # Functionality to display current loans
        pass

    def quit_fullscreen(self, event):
        self.attributes("-fullscreen", False)  # Exit fullscreen

def main():
    app = FullScreenApp()
    app.mainloop()

if __name__ == "__main__":
    main()
