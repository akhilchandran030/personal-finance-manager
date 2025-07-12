import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime


root = tk.Tk()
root.title("Personal Finance Manager")
root.geometry("400x350")
root.configure(bg="#f5f5f5")

# Title
tk.Label(
    root, text="Enter Your Expense", font=("Arial", 14, "bold"), bg="#f5f5f5"
).pack(pady=10)

# Date input
tk.Label(root, text="Date (DD-MM-YYYY):", bg="#f5f5f5").pack()
date_entry = tk.Entry(root, width=30)
date_entry.pack(pady=5)

# Category input
tk.Label(root, text="Category:", bg="#f5f5f5").pack()
category_entry = tk.Entry(root, width=30)
category_entry.pack(pady=5)

# Amount input
tk.Label(root, text="Amount (Rs.):", bg="#f5f5f5").pack()
amount_entry = tk.Entry(root, width=30)
amount_entry.pack(pady=5)


# Save to CSV
def save_data():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()

    #Validate date format
    try:
        datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        messagebox.showerror("Invalid Date", "Date must be in DD-MM-YYYY format")
        return

    #Validate amount as number (can be float)
    try:
        float(amount)
    except ValueError:
        messagebox.showerror("Invalid Input", "Amount must be a number")
        return

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    messagebox.showinfo("Success", "Expense saved!")

    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)


# Save button
tk.Button(
    root, text="Save Expense", command=save_data, bg="#4CAF50", fg="white", width=20
).pack(pady=20)

root.mainloop()
