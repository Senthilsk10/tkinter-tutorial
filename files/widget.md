## Tkinter Form Submission Example

This repository contains a simple example of creating a form with Tkinter in Python and submitting the form data.

### Code Explanation

- **Syntax:** `import tkinter as tk`
  - **Explanation:** Imports the Tkinter module and aliases it as `tk` for ease of use.

- **Syntax:** `def submit_form():`
  - **Explanation:** Defines a function `submit_form()` that prints the form data when the Submit button is clicked.

- **Syntax:** `root = tk.Tk()`
  - **Explanation:** Creates the main application window.

- **Syntax:** `name_label = tk.Label(root, text="Name:")`
  - **Explanation:** Creates a label widget with the text "Name:".

- **Syntax:** `name_label.grid(row=0, column=0, padx=10, pady=5)`
  - **Explanation:** Places the name label in the first row and first column of the grid layout, with horizontal padding of 10 pixels and vertical padding of 5 pixels.

- **Syntax:** `name_entry = tk.Entry(root)`
  - **Explanation:** Creates an entry widget for entering the name.

- **Syntax:** `name_entry.grid(row=0, column=1, padx=10, pady=5)`
  - **Explanation:** Places the name entry widget in the first row and second column of the grid layout, with horizontal padding of 10 pixels and vertical padding of 5 pixels.

- **Syntax:** `gender = tk.StringVar()`
  - **Explanation:** Creates a StringVar object to hold the value of the selected gender.

- **Syntax:** `male_radio = tk.Radiobutton(root, text="Male", variable=gender, value="Male")`
  - **Explanation:** Creates a radio button widget for selecting Male gender and associates it with the gender variable.

- **Syntax:** `male_radio.grid(row=2, column=1, padx=10, pady=5)`
  - **Explanation:** Places the Male radio button widget in the third row and second column of the grid layout, with horizontal padding of 10 pixels and vertical padding of 5 pixels.

- **Syntax:** `subscribe = tk.BooleanVar()`
  - **Explanation:** Creates a BooleanVar object to hold the value of the subscription checkbox.

- **Syntax:** `subscribe_checkbox = tk.Checkbutton(root, text="Subscribe", variable=subscribe)`
  - **Explanation:** Creates a checkbox widget for subscribing to notifications and associates it with the subscribe variable.

- **Syntax:** `subscribe_checkbox.grid(row=3, columnspan=2, padx=10, pady=5)`
  - **Explanation:** Places the subscription checkbox widget in the fourth row, spanning two columns of the grid layout, with horizontal padding of 10 pixels and vertical padding of 5 pixels.

- **Syntax:** `submit_button = tk.Button(root, text="Submit", command=submit_form)`
  - **Explanation:** Creates a button widget with the text "Submit" that calls the submit_form function when clicked.

- **Syntax:** `submit_button.grid(row=4, columnspan=2, padx=10, pady=10)`
  - **Explanation:** Places the submit button widget in the fifth row, spanning two columns of the grid layout, with horizontal padding of 10 pixels and vertical padding of 10 pixels.

### Comments

- The form consists of labels, entry fields, radio buttons, and a checkbox widget for collecting user information.
- Widgets are organized using the grid layout manager to create a structured form layout.
- The form data is printed to the console when the Submit button is clicked.
