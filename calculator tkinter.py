import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")  # Set a fixed size
root.configure(bg="#2C3E50")  # Background color

# Entry widget for the display
entry = tk.Entry(root, width=25, borderwidth=5, font=('Arial', 24), justify='right', bg="#ECF0F1", fg="#34495E")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Define the button labels and positions
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Styling for the buttons
button_colors = {
    "numbers": {"bg": "#1ABC9C", "fg": "#ECF0F1"},
    "operations": {"bg": "#3498DB", "fg": "#ECF0F1"},
    "clear": {"bg": "#E74C3C", "fg": "#ECF0F1"},
    "equal": {"bg": "#2ECC71", "fg": "#ECF0F1"}
}

# Create and place buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), 
                           bg=button_colors["equal"]["bg"], fg=button_colors["equal"]["fg"],
                           command=calculate)
    elif text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), 
                           bg=button_colors["clear"]["bg"], fg=button_colors["clear"]["fg"],
                           command=clear_entry)
    elif text in '+-*/':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), 
                           bg=button_colors["operations"]["bg"], fg=button_colors["operations"]["fg"],
                           command=lambda t=text: button_click(t))
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 18), 
                           bg=button_colors["numbers"]["bg"], fg=button_colors["numbers"]["fg"],
                           command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# Adjust row and column weights for responsive layout
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

# Run the main application loop
root.mainloop()
