import tkinter as tk

def button_click():
    label.config(text="Button Clicked!")

root = tk.Tk()

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

button = tk.Button(root, text="Click Me", command=button_click)
button.pack()

entry = tk.Entry(root)
entry.pack()

text = tk.Text(root)
text.pack()

frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame.pack()

checkbutton = tk.Checkbutton(root, text="Check Me")
checkbutton.pack()

radio_button_var = tk.StringVar()
radio_button1 = tk.Radiobutton(root, text="Option 1", variable=radio_button_var, value="Option 1")
radio_button1.pack()
radio_button2 = tk.Radiobutton(root, text="Option 2", variable=radio_button_var, value="Option 2")
radio_button2.pack()


root.mainloop()
