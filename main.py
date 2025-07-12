import tkinter as tk

root = tk.Tk()
root.title("Personal Finance Manager")
root.geometry("400x300")
root.configure(bg="#f5f5f5")

label = tk.Label(root, text="Welcome to Personal Finance Manager", font=("Arial", 14), bg="#f5f5f5", wraplength=300)
label.pack(pady=30)

root.mainloop()
