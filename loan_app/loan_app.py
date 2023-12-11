# loan_app.py

from gui.main_loan_window import LoanManagerApp
import tkinter as tk

def start_loan_app():
    root = tk.Tk()
    app = LoanManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    start_loan_app()

