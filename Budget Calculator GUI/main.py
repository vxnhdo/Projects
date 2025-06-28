# 1. Import libraries for GUI
import tkinter as tk # Python GUI library
from tkinter import messagebox # For error pop-ups 

# 2. Create Main Window
window = tk.Tk() # Set main application window
window.title("Budget Calculator") # Window title
window.geometry("400x350") # Set window size
window.resizable(False, False) # Disable horizontal & vertical resizing

# 3. Center the Window on Screen
window.update_idletasks() # Forces layout calculation
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2) # Get window dimensions
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}") # x & y are coordinates to place the window in the middle

# 4. CREATE A FRAME (CONTAINER)
frame = tk.Frame(window, padx=20, pady=20) # Groups widgets together, add padding inside the frame
frame.pack(fill="both", expand=True) # Places frame inside the window and allows expand

# 5. Set Fonts
label_font = ("Arial", 12) # defines font style & size for readability
entry_font = ("Arial", 12)

# 6. Label and Entry Fields
tk.Label(frame, text="Monthly Income:", font=label_font).grid(row=0, column=0, sticky="w", pady=5) # sticky="w" = Aligns label text to the left
entry_income = tk.Entry(frame, font=entry_font)
entry_income.grid(row=0, column=1, pady=5, padx=10, sticky="e") # Places widgets in a grid layout using rows & columns, adds spacing between widgets

tk.Label(frame, text="Rent: ", font=label_font).grid(row=1, column=0, sticky="w", pady=5)
entry_rent = tk.Entry(frame, font=entry_font)
entry_rent.grid(row=1, column=1, pady=5, padx=10, sticky="e")

tk.Label(frame, text="Groceries: ", font=label_font).grid(row=2, column=0, sticky="w", pady=5)
entry_groceries = tk.Entry(frame, font=entry_font)
entry_groceries.grid(row=2, column=1, pady=5, padx=10, sticky="e")

tk.Label(frame, text="Transport: ", font=label_font).grid(row=3, column=0, sticky="w", pady=5)
entry_transport = tk.Entry(frame, font=entry_font)
entry_transport.grid(row=3, column=1, pady=5, padx=10, sticky="e")

tk.Label(frame, text="Utilities: ", font=label_font).grid(row=4, column=0, sticky="w", pady=5)
entry_utilities = tk.Entry(frame, font=entry_font)
entry_utilities.grid(row=4, column=1, pady=5, padx=10, sticky="e")

# Function to Calculate Budget to run when "Calculate" button is clicked
def calculate_budget():
    try:
        income = float(entry_income.get()) # Retrieves the user input from each entry box, converts input into a number
        rent = float(entry_rent.get())
        groceries = float(entry_groceries.get())
        transport = float(entry_transport.get())
        utilities = float(entry_utilities.get())

        total_expenses = rent + groceries + transport + utilities
        savings = income - total_expenses

        result_text = (
            f"Total Income: ${income:.2f}\n"
            f"Total Expenses: ${total_expenses:.2f}\n"
            f"Total Savings: ${savings:.2f}\n"
        )

        if savings > 0:
            result_text += "Saving this month."
        elif savings == 0:
            result_text += "Broke even this month."
        else:
            result_text += "Overspending this month."

        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number for all fields.")
        return
    
# Calculate Button
tk.Button(frame, text="Calculate", command=calculate_budget, font=("Arial", 11, "bold")).grid(row=5, column=0, columnspan=2, pady=15)

# Display Result
result_label = tk.Label(frame, text="", justify="left", font=("Arial", 12))
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Run GUI Loop
window.mainloop()

