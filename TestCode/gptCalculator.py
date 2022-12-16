# Import the Tkinter module
import Tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the input fields and buttons
input_field = tk.Entry(root)
input_field.grid(row=0, column=0, columnspan=3)

button1 = tk.Button(root, text="1", command=lambda: input_field.insert(tk.END, "1"))
button1.grid(row=1, column=0)
button2 = tk.Button(root, text="2", command=lambda: input_field.insert(tk.END, "2"))
button2.grid(row=1, column=1)
button3 = tk.Button(root, text="3", command=lambda: input_field.insert(tk.END, "3"))
button3.grid(row=1, column=2)

# Add more buttons for the other digits and operations

# Run the main loop to display the calculator
root.mainloop()

import Tkinter
import sys

print(sys.modules['tkinter'].__file__)