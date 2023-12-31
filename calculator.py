import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(tk.END, result)

# Create the main window
window = tk.Tk()
window.title("Dan's Calculator")  # Set the root title

# Create an entry widget to display the input and output
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Create number buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

for button_text, row, column in buttons:
    button = tk.Button(window, text=button_text, width=5, command=lambda text=button_text: button_click(text))
    button.grid(row=row, column=column)

# Create clear button
clear_button = tk.Button(window, text="C", width=5, command=button_clear)
clear_button.grid(row=5, column=0)

# Create equal button
equal_button = tk.Button(window, text="=", width=5, command=button_equal)
equal_button.grid(row=5, column=1)

# Run the main loop
window.mainloop()
