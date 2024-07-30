# Personal Finance Tracker
# Description: Build an application that helps users track their personal finances, including income, expenses, and budgeting. The application should allow users to input their financial transactions and categorize them (e.g., groceries, utilities, salary). It could also provide simple statistics on spending.

# Minimum Requirements:

# Create functions for different financial calculations and operations (e.g., adding transactions, categorizing expenses, calculating totals).
# Use Python’s standard libraries for working with dates and currency.
# Store financial data in a suitable container, allowing for filtering and sorting by date, category, etc.
# Implement TDD using pytest for your financial calculations and operations.
# Explore third-party libraries for data visualization (e.g., Matplotlib or Plotly) to show spending trends over time.

#----------------------------------------------------------------------------------------------------
# Key Features:

# Add Expenses: Users can input their expenses by providing the date (in YYYY-MM-DD format), expense category, and the amount spent. The application stores this information in a text file named "expenses.txt" for future reference.

# View Expenses: The Expense Tracker displays all recorded expenses in a tabular format. It presents details such as the date, expense category, and amount, along with a total expense calculated from the accumulated amounts.

# Delete Expenses: Users can delete any unwanted expense from the list by selecting the corresponding entry and clicking the "Delete Expense" button. The entry will be removed from both the GUI and the "expenses.txt" file.

#----Code starts here ------
import os
import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib as plt
# import add, delete, view 

def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()

    if date and category and amount:
        with open("expenses.txt", "a") as file:
            file.write(f"{date},{category},{amount}\n")
        status_label.config(text="Expense added successfully!", fg="green")
        date_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
        amount_entry.delete(0, tk.END)
        view_expenses()
    else:
        status_label.config(text="Please fill all the fields!", fg="red")

def delete_expense():
    selected_item = expenses_tree.selection()
    if selected_item:
        item_text = expenses_tree.item(selected_item, "values")
        date, category, amount = item_text
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
        with open("expenses.txt", "w") as file:
            for line in lines:
                if line.strip() != f"{date},{category},{amount}":
                    file.write(line)
        status_label.config(text="Expense deleted successfully!", fg="green")
        view_expenses()
    else:
        status_label.config(text="Please select an expense to delete!", fg="red")

def view_expenses():
    global expenses_tree
    if os.path.exists("expenses.txt"):
        total_expense = 0
        expenses_tree.delete(*expenses_tree.get_children())
        with open("expenses.txt", "r") as file:
            for line in file:
                date, category, amount = line.strip().split(",")
                expenses_tree.insert("", tk.END, values=(date, category, amount))
                total_expense += float(amount)
        total_label.config(text=f"Total Expense: {total_expense:.2f}")
    else:
        total_label.config(text="No expenses recorded.")
        expenses_tree.delete(*expenses_tree.get_children())

# Create the main application window
root = tk.Tk()
# root.geometry("750x750")
root.title("My Expenses Tracker")


# Create labels and entries for adding expenses
date_label = tk.Label(root, text="Date (YYYY-MM-DD):", fg='blue')
date_label.grid(row=0, column=0, padx=5, pady=5)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1, padx=5, pady=5)

category_label = tk.Label(root, text="Category:", fg='blue')
category_label.grid(row=1, column=0, padx=5, pady=5)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1, padx=5, pady=5)

amount_label = tk.Label(root, text="Amount:", fg='blue')
amount_label.grid(row=2, column=0, padx=5, pady=5)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# Create a treeview to display expenses
columns = ("Date", "Category", "Amount")
expenses_tree = ttk.Treeview(root, columns=columns, show="headings")
expenses_tree.heading("Date", text="Date")
expenses_tree.heading("Category", text="Category")
expenses_tree.heading("Amount", text="Amount")
expenses_tree.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Create a label to display the total expense
total_label = tk.Label(root, text="")
total_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Create a label to show the status of expense addition and deletion
status_label = tk.Label(root, text="", fg="green")
status_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Create buttons to view and delete expenses
view_button = tk.Button(root, text="View Expenses", command=view_expenses)
view_button.grid(row=7, column=0, padx=5, pady=10)

delete_button = tk.Button(root, text="Delete Expense", command=delete_expense)
delete_button.grid(row=7, column=1, padx=5, pady=10)

# Check if the 'expenses.txt' file exists; create it if it doesn't
if not os.path.exists("expenses.txt"):
    with open("expenses.txt", "w"):
        pass

# Display existing expenses on application start
view_expenses()

def plot_expenses(expenses):
    df = pd.DataFrame(list(expenses.items()), columns=['Category', 'Amount'])
    df.plot(kind='bar', x='Category', y='Amount', legend=False)
    plt.ylabel('Amount ($)')
    plt.title('Expense Distribution')
    plt.show()

#remove the default icon on title bar
root.wm_attributes('-toolwindow', 'True')

root.mainloop()
