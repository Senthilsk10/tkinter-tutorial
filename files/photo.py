import tkinter as tk
from tkinter import PhotoImage

def display_image():
    file_path = entry.get()
    try:
        image = PhotoImage(file=file_path)
        image_label.config(image=image)
        image_label.image = image  
    except:
        print("Invalid image path or format.")

root = tk.Tk()
root.title("Image Viewer")

entry = tk.Entry(root, width=50)
entry.pack()

open_button = tk.Button(root, text="Display Image", command=display_image)
open_button.pack()

image_label = tk.Label(root)
image_label.pack()

root.mainloop()
