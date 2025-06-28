# Create a GUI app using Python and Tkinter to manage student records.
# Create a DB table with Add, Update and Delete ability
# Display records automatically from the start

import tkinter as tk                    # import the Tkinter module & assigns it to variable 'tk'
from tkinter import ttk, messagebox     # import ttk for themed widgets and messagebox for dialog boxes
import sqlite3                          # import built=in SQLite3 module to connect to SQLite database   

# Ensure database exists and set it up
# Connect a db file named 'students.db' & use conn as the connection object used to interact with the database
# Create a cursor object from the connection to execute SQL commands
conn = sqlite3.connect("students.db")
c = conn.cursor()
# Create a table named 'students' if it does not already exist
# Each field must have a value, so we set NOT NULL for each field
# If no value is provided for 'enrolled', it defaults to 0 (not enrolled)
c.execute(''' 
    CREATE TABLE IF NOT EXISTS students (
        grad_year TEXT NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        gender TEXT NOT NULL,
        department TEXT NOT NULL,
        enrolled INTEGER NOT NULL DEFAULT 0
    )
''')
conn.commit() # saves / commits anyu changes made to the db
conn.close()  # closes the connection to the database

class StudentApp: # Defines a python class named StudentApp, will contain all GUI logic & event handlers     
    def __init__(self, root):  # Constructor method to initialize the app
        self.root = root       # Stores main window as an attribute of the class 
        self.root.title("Student Management System")        # Sets then title of the main window
        self.root.configure(bg='#f8f9fa')                 # Sets the background color of the main window
        self.root.geometry("1000x600")                      # Sets the size of the main window to 1000x600px

        try:        # Attempt to load an icon for the main window
            self.icon = tk.PhotoImage(file="Student-Male-icon.png")
            self.root.iconphoto(False, self.icon)
        except Exception as e:      # If file is NOT found, print an error message
            print("Icon not found or failed to load.", e)

        self.gender_var = tk.StringVar(value="Male") # Create a string variable with value of "Male"
        self.dept_var = tk.StringVar()               # Create a string variable to hold department name, empty by default
        self.grad_year_var = tk.StringVar()          # Create a string var to hold graduation year, empty by default
        self.enrolled_var = tk.IntVar(value=0)       # Create an integer variable to hold enrollment status, default is 0 (not enrolled)

        self.setup_ui()     # Calls the setup_ui method to create all widgets and layout   
        self.refresh_tree() # Calls the refresh_tree method to display in treeview with existing records

    # Function to set up the user interface in main window self.root
    def setup_ui(self):
        # Define a style for labels
        label_style = {'bg': '#f8f9fa', 'fg': '#212529', 'font': ('Segoe UI', 11)} 
        entry_style = {'bg': '#ffffff', 'fg': '#212529', 'font': ('Segoe UI', 11)}

        # Create a header frame to hold the title and icon
        header_frame = tk.Frame(self.root, bg='#f8f9fa')
        header_frame.grid(row=0, column=0, columnspan=5, sticky='ew', pady=(10, 20)) # Place frame on row 0, column 0, spanning 5 columns, frame will expand horizontally & add verticaly paddubg

        # Try to load header icon
        try:
            self.corner_icon = tk.PhotoImage(file="10207-man-student-light-skin-tone-icon.png")
            image_label = tk.Label(header_frame, image=self.corner_icon, bg="#f8f9fa")
            image_label.pack(side='left', padx=10)
        except Exception as e: # If icon file is not found, print an error message
            print("Header icon not found or failed to load.", e)

        # Create a header label with title text with styling
        header = tk.Label(header_frame, text="Student Information Database", 
                          bg='#f8f9fa', fg='#212529', 
                          font=('Segoe UI Semibold', 24, 'bold'))
        header.pack(side='left') # Add header label to the left side of the header frame

        # Use a loop to ensure each column in resizeable by using weight=1
        for i in range(5):
            self.root.grid_columnconfigure(i, weight=1)

        # Add a "Graduation Year" label and dropdown menu of a list of years from 2025-2035
        tk.Label(self.root, text="Graduation Year:", **label_style).grid(row=1, column=0, padx=5, pady=5, sticky='e') # right-align
        grad_years = [str(year) for year in range(2025, 2036)]
        self.grad_year_option = tk.OptionMenu(self.root, self.grad_year_var, *grad_years)
        self.grad_year_option.config(bg='#ffffff', fg='#212529', font=('Segoe UI', 11))
        self.grad_year_option.grid(row=1, column=1, padx=5, pady=5, sticky='w') # left-align

        # Add a First Name label and text entry field box for user input
        tk.Label(self.root, text="First Name:", **label_style).grid(row=2, column=0, padx=5, pady=5, sticky='e')
        self.first_name_entry = tk.Entry(self.root, **entry_style)
        self.first_name_entry.grid(row=2, column=1, padx=5, pady=5, sticky='w')

        # Add a Last Name label and text entry field box for user input
        tk.Label(self.root, text="Last Name:", **label_style).grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.last_name_entry = tk.Entry(self.root, **entry_style)
        self.last_name_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        # Gender selection using radio buttons, create a frame to hold them side by side & only one can be selected at a time
        tk.Label(self.root, text="Gender:", **label_style).grid(row=4, column=0, padx=5, pady=5, sticky='e')
        gender_frame = tk.Frame(self.root, bg='#f8f9fa')
        gender_frame.grid(row=4, column=1, padx=5, pady=5, sticky='w')
        tk.Radiobutton(gender_frame, text="Male", variable=self.gender_var, value="Male",
                       bg='#f8f9fa', fg='#333333', font=('Segoe UI Semibold', 10, 'bold')).pack(side='left')
        tk.Radiobutton(gender_frame, text="Female", variable=self.gender_var, value="Female",
                       bg='#f8f9fa', fg='#333333', font=('Segoe UI Semibold', 10, 'bold')).pack(side='left')

        # Department label and define a dropdown menu with a list of departments, only one can be selected at a time
        tk.Label(self.root, text="Department:", **label_style).grid(row=5, column=0, padx=5, pady=5, sticky='e')
        departments = [
            "Computer Science", "Math", "English", "Physics", "Biology",
            "Chemistry", "History", "Art", "Music", "Economics",
            "Political Science", "Sociology", "Psychology", "Philosophy", "Engineering"
        ]
        self.dept_option = ttk.Combobox(self.root, textvariable=self.dept_var, values=departments, state="readonly",
                                        font=('Segoe UI', 11))
        self.dept_option.grid(row=5, column=1, padx=5, pady=5, sticky='w')

        # Enrolled status checkbox, default is unchecked (0)
        self.enrolled_checkbox = tk.Checkbutton(self.root, text="Enrolled", variable=self.enrolled_var,
                                                bg='#f8f9fa', fg='#212529', font=('Segoe UI', 11))
        self.enrolled_checkbox.grid(row=6, column=1, padx=5, pady=5, sticky='w')

        # Buttons for Add, Update, Delete, and Exit actions
        # Create a frame to hold buttons and add them to the frame
        btn_frame = tk.Frame(self.root, bg='#f8f9fa')
        btn_frame.grid(row=7, column=0, columnspan=3, pady=10, sticky='w') # Frame on row 7, spanning 3 columns, + vertical padding & left-align

        tk.Button(btn_frame, text="Add", command=self.add_record, bg='#a1c6ea', font=('Segoe UI', 10)).pack(side='left', padx=5) # add student
        tk.Button(btn_frame, text="Update", command=self.update_record, bg='#a1c6ea', font=('Segoe UI', 10)).pack(side='left', padx=5) # update student
        tk.Button(btn_frame, text="Delete", command=self.delete_record, bg='#ef9a9a', font=('Segoe UI', 10)).pack(side='left', padx=5) # delete student        
        tk.Button(btn_frame, text="Exit", command=self.root.destroy, bg='#ef9a9a', font=('Segoe UI', 10)).pack(side='left', padx=5) # exit app

        # Treeview widget to display student records
        columns = ("Graduation Year", "First Name", "Last Name", "Gender", "Department", "Enrolled") # defines each column
        self.tree = ttk.Treeview(self.root, columns=columns, show='headings', height=15) 

        # Add headers for each column, set column widths & center alignment            
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120 if col != "Enrolled" else 70, anchor='center')

        # Place treeview in column 3, starting from row 1, spanning 6 rows vertically
        self.tree.grid(row=1, column=3, rowspan=6, padx=10, pady=10, sticky='nsew')
        self.tree.bind("<<TreeviewSelect>>", self.load_selected_record) # When a record is selected, call load_selected_record method to load student's data into the input form


        # Add a vertical scrollbar to the treeview
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview) # Link it to the treeview's yview
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, column=4, rowspan=6, sticky='ns', pady=10)                 # Place in column 4, spanning 6 rows, aligned vertically

        self.root.grid_columnconfigure(3, weight=1)                                      # Make the treeview column resizable

        # Add status bar at the bottom of the window with initial text "Ready"
        self.status_bar = tk.Label(self.root, text="Ready", bg='green', fg='white', font=('Segoe UI', 12), anchor='center')
        self.status_bar.grid(row=8, column=0, columnspan=5, sticky='ew', pady=(10, 0))


    # Function to add a new student record to the database
    def add_record(self):
        # Fetch the values from user input
        grad_year = self.grad_year_var.get() 
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        gender = self.gender_var.get()
        department = self.dept_var.get()
        enrolled = self.enrolled_var.get()

        # Validate input fields
        # Ensure all required fields are filled in
        if not grad_year or not first_name or not last_name or not department:
            messagebox.showwarning("Input error", "Please fill in all required fields")
            return

        # Connect to db file & create a cursor object
        conn = sqlite3.connect("students.db")
        c = conn.cursor()

        # Insert the new row into the students table, using placeholders so data can be safely passed
        c.execute("INSERT INTO students (grad_year, first_name, last_name, gender, department, enrolled) VALUES (?, ?, ?, ?, ?, ?)",
                  (grad_year, first_name, last_name, gender, department, enrolled))
        
        # Commit the changes to the database and close the connection
        conn.commit() 
        conn.close()

        # Clear the input fields, then refresh the treeview, and show a success dialog popup
        self.clear_entries()
        self.refresh_tree()
        self.show_success_dialog()

    # Function to update an existing student record in the database
    def update_record(self):
        selected = self.tree.selection()
        if not selected:
            return
        item = self.tree.item(selected[0])
        old_grad_year, old_first_name, old_last_name = item['values'][0:3]

        grad_year = self.grad_year_var.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        gender = self.gender_var.get()
        department = self.dept_var.get()
        enrolled = self.enrolled_var.get()

        conn = sqlite3.connect("students.db")
        c = conn.cursor()
        c.execute('''
            UPDATE students
            SET grad_year = ?, first_name = ?, last_name = ?, gender = ?, department = ?, enrolled = ?
            WHERE grad_year = ? AND first_name = ? AND last_name = ?
        ''', (grad_year, first_name, last_name, gender, department, enrolled, old_grad_year, old_first_name, old_last_name))
        conn.commit()
        conn.close()
        self.clear_entries()
        self.refresh_tree()
        self.show_success_dialog()

    # Function to delete a selected student record from the database
    def delete_record(self):
        # Check if a record is selected in the treeview, if not return
        selected = self.tree.selection()
        if not selected:
            return
        
        # Get the data of the selected record & extract the values needed to delete the record
        item = self.tree.item(selected[0])
        grad_year, first_name, last_name = item['values'][0:3]

        # Connect to the database and create a cursor object
        conn = sqlite3.connect("students.db")
        c = conn.cursor()

        # Update the record in the students table using a WHERE clause to match the record to be deleted
        c.execute("DELETE FROM students WHERE grad_year = ? AND first_name = ? AND last_name = ?",
                  (grad_year, first_name, last_name))
        
        # Commit the changes to the database and close the connection
        conn.commit()
        conn.close()

        # Clear the input fields, refresh the treeview, and show a success dialog popup
        self.clear_entries()
        self.refresh_tree()

    # Function to be called when a user selects a record in the treeview so that the data can be loaded into the input fields
    def load_selected_record(self, event):

        # Return a list of selected items in the treeview, if no item is selected, return
        selected = self.tree.selection()
        if not selected:
            return
        
        # Get the data of the selected record and set the input fields with the values
        # 'values' = tuple of values for each column in the selected row
        data = self.tree.item(selected[0])['values']
        self.grad_year_var.set(data[0])             # Set the graduation year variable to the selected graduation year
        self.first_name_entry.delete(0, 'end')      # Clear the first name entry field
        self.first_name_entry.insert(0, data[1])    # Insert the selected first name into the entry field
        self.last_name_entry.delete(0, 'end')       # Clear the last name entry field
        self.last_name_entry.insert(0, data[2])     # Insert the selected last name into the entry field
        self.gender_var.set(data[3])                # Set the gender radio button 
        self.dept_var.set(data[4])                  # Set the department dropdown menu       
        self.enrolled_var.set(data[5])              # Set the enrolled checkbox to the selected value (0 or 1)


    # Function to clear all input fields and reset the form
    def clear_entries(self):
        self.grad_year_var.set("")                  # Clear graduation year dropdown
        self.first_name_entry.delete(0, 'end')      # Clear first name entry field
        self.last_name_entry.delete(0, 'end')       # Clear last name entry field
        self.gender_var.set("Male")                 # Reset gender as Male by default
        self.dept_var.set("")                       # Clear department dropdown
        self.enrolled_var.set(0)                    # Uncheck enrolled checkbox to 0 


    # Function to refresh the treeview with the latest records from the database
    def refresh_tree(self):
        # Clear all existing records in the treeview
        for i in self.tree.get_children():
            self.tree.delete(i)
        
        # Connect to the db, create a cursor object
        conn = sqlite3.connect("students.db")
        c = conn.cursor()

        # Fetch all records from the students table
        c.execute("SELECT * FROM students")
        rows = c.fetchall() # retrieves all rows as a list of tuples

        # Insert each row into the treeview
        for row in rows:
            self.tree.insert('', 'end', values=row) # Insert at root level, add to the bottom of treeview & fills the columns with the row values
        conn.close()                                # close db connection

    # Function to show a success dialog popup and update the status bar
    def show_success_dialog(self):
        self.status_bar.config(text="Success!", bg='blue')                              # Update status bar text and color
        self.root.after(2000, lambda: self.status_bar.config(text="Ready", bg='green')) # Reset status bar after 2 seconds

if __name__ == "__main__": # check if script is run directly, if true, do the following
    root = tk.Tk()         # Create the main window 
    app = StudentApp(root) # Create an instance of app, passing the root window as the argument
    root.mainloop()        # Start the Tkinter event loop to run the app
