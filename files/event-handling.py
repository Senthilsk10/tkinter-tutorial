import tkinter as tk

def on_hover(event):
    print("Mouse hovered over the button")

def on_double_click(event):
    print("Button double-clicked")
    
def handlechange(event):
    print("pressed")
    print(text.get())

root = tk.Tk()
root.geometry("300x200")

button = tk.Button(root, text="Click me")
button.pack(pady=20)

# Bind events to the button widget
button.bind("<Enter>", on_hover)  # Mouse hover
button.bind("<Double-Button-1>", on_double_click)  # Double-click

# Create a text entry widget
text = tk.StringVar()
entry = tk.Entry(root,textvariable=text)
entry.pack(pady=10)

# Bind events to the entry widget
entry.bind("<KeyRelease>", handlechange)  # Double-click

root.mainloop()
