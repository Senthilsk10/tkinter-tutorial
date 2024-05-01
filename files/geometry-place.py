import tkinter as tk

root = tk.Tk()
root.title("Place Example")
root.geometry("300x200")

label1 = tk.Label(root, text="Label 1", bg="lightblue")
label1.place(x=50, y=50)  # Specify x and y coordinates

label2 = tk.Label(root, text="Label 2", bg="lightgreen")
label2.place(relx=0.10, rely=0.10)  # Specify relative x and y coordinates

label3 = tk.Label(root, text="Label 3", bg="lightcoral")
label3.place(x=200, y=150,width=50,height=25)  # Specify x and y coordinates, and width and height

root.mainloop()
