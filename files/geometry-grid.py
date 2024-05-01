import tkinter as tk

root = tk.Tk()
root.title("Grid Example")
root.geometry("300x200")

label1 = tk.Label(root, text="Label 1", bg="lightblue")
label1.grid(row=0, column=0, padx=5, pady=5,rowspan=2)  # Adding padding and rowsspan

label2 = tk.Label(root, text="Label 2", bg="lightgreen")
label2.grid(row=1, column=0, padx=5, pady=5)  # Adding padding

label3 = tk.Label(root, text="Label 3", bg="lightcoral")
label3.grid(row=0, column=1, padx=5, pady=5, columnspan=2)  # Adding padding and columnspan

label4 = tk.Label(root, text="Label 4", bg="lightyellow")
label4.grid(row=1, column=1, padx=5, pady=5)  # Adding padding

label5 = tk.Label(root, text="Label 5", bg="lightpink")
label5.grid(row=1, column=2, padx=5, pady=5)  # Adding padding

root.mainloop()
