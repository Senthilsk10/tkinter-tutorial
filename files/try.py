'''
from tkinter.simpledialog import askstring
from tkinter import *

top = Tk()

top.geometry("400x400")
def show():
   name = askstring("Input", "Enter you name")
   print(name)
   
B = Button(top, text ="Click", command = show)
B.place(x=50,y=50)

top.mainloop()
'''

#program for converting fahrenheit to celsius
'''
import tkinter as tk

def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    fahrenheit = ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

# Set up the window
window = tk.Tk()
window.title("Temperature Converter")
window.resizable(width=False, height=False)

# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Set up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

# Run the application
window.mainloop()'''


#sample app for displaying messages that entered by the user
'''import tkinter as tk

def greeting():
    label.config(text="Hello, " + entry.get())

root = tk.Tk()

label = tk.Label(root, text="Enter your name:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Greet", command=greeting)
button.pack()

root.mainloop()'''



#sample app for entering , clearing , displaying messages
'''import tkinter as tk
from tkinter import messagebox

# Function to display text on label
def display_text():
    text = input_text.get()
    if text:
        label_text.config(text="You entered: " + text)
    else:
        messagebox.showerror("Error", "Please enter some text.")

# Function to clear the input field
def clear_input():
    input_text.delete(0, tk.END)
    label_text.config(text="")

# Initialize the root window
root = tk.Tk()
root.title("Tkinter Example Application")

# Create a label for input instruction
label_input = tk.Label(root, text="Enter text:")
label_input.pack()

# Create an entry for text input
input_text = tk.Entry(root)
input_text.pack()

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Create a button to display text
button_display = tk.Button(button_frame, text="Display", command=display_text)
button_display.pack(side=tk.LEFT, padx=5)

# Create a button to clear input
button_clear = tk.Button(button_frame, text="Clear", command=clear_input)
button_clear.pack(side=tk.LEFT, padx=5)

# Create a label to display the input text
label_text = tk.Label(root, text="")
label_text.pack()

# Run the main loop
root.mainloop()'''