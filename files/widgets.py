import tkinter as tk

def submit_form():
    print("Form submitted!")
    print("Name:", name_entry.get())
    print("Email:", email_entry.get())
    print("Gender:", gender.get())
    print("Subscribe:", subscribe.get())

root = tk.Tk()
root.title("Widget Tutorial")


name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0, padx=10, pady=5)

gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=2, column=0, padx=10, pady=5)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

gender = tk.StringVar()
male_radio = tk.Radiobutton(root, text="Male", variable=gender, value="Male")
male_radio.grid(row=2, column=1, padx=10, pady=5)

female_radio = tk.Radiobutton(root, text="Female", variable=gender, value="Female")
female_radio.grid(row=2, column=2, padx=10, pady=5)

subscribe = tk.BooleanVar()
subscribe_checkbox = tk.Checkbutton(root, text="Subscribe", variable=subscribe)
subscribe_checkbox.grid(row=3, columnspan=2, padx=10, pady=5)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4, columnspan=2, padx=10, pady=10)

root.mainloop()

