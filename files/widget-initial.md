## Tkinter Widget Examples

This repository contains a simple example of creating various GUI (Graphical User Interface) widgets using Tkinter in Python.

### Code Explanation

- **Syntax:** `import tkinter as tk`
  - **Explanation:** Imports the Tkinter module and aliases it as `tk` for ease of use.

- **Syntax:** `def button_click():`
  - **Explanation:** Defines a function `button_click()` that updates the text of the label widget when a button is clicked.

- **Syntax:** `root = tk.Tk()`
  - **Explanation:** Creates the main application window.

- **Syntax:** `label = tk.Label(root, text="Hello, Tkinter!")`
  - **Explanation:** Creates a label widget with the text "Hello, Tkinter!".

- **Syntax:** `label.pack()`
  - **Explanation:** Packs the label widget into the root window.

- **Syntax:** `button = tk.Button(root, text="Click Me", command=button_click)`
  - **Explanation:** Creates a button widget with the text "Click Me" and associates it with the `button_click()` function.

- **Syntax:** `button.pack()`
  - **Explanation:** Packs the button widget into the root window.

- **Syntax:** `entry = tk.Entry(root)`
  - **Explanation:** Creates an entry widget for user input.

- **Syntax:** `entry.pack()`
  - **Explanation:** Packs the entry widget into the root window.

- **Syntax:** `text = tk.Text(root)`
  - **Explanation:** Creates a text widget for displaying multi-line text.

- **Syntax:** `text.pack()`
  - **Explanation:** Packs the text widget into the root window.

- **Syntax:** `frame = tk.Frame(root, bd=2, relief=tk.SUNKEN)`
  - **Explanation:** Creates a frame widget with a border width of 2 pixels and a sunken relief style.

- **Syntax:** `frame.pack()`
  - **Explanation:** Packs the frame widget into the root window.

- **Syntax:** `checkbutton = tk.Checkbutton(root, text="Check Me")`
  - **Explanation:** Creates a checkbutton widget with the text "Check Me".

- **Syntax:** `checkbutton.pack()`
  - **Explanation:** Packs the checkbutton widget into the root window.

- **Syntax:** `radio_button_var = tk.StringVar()`
  - **Explanation:** Creates a StringVar object to hold the value of the selected radio button.

- **Syntax:** `radio_button1 = tk.Radiobutton(root, text="Option 1", variable=radio_button_var, value="Option 1")`
  - **Explanation:** Creates a radio button widget with the text "Option 1" and associates it with the radio_button_var variable.

- **Syntax:** `radio_button1.pack()`
  - **Explanation:** Packs the radio button widget into the root window.

- **Syntax:** `radio_button2 = tk.Radiobutton(root, text="Option 2", variable=radio_button_var, value="Option 2")`
  - **Explanation:** Creates a radio button widget with the text "Option 2" and associates it with the radio_button_var variable.

- **Syntax:** `radio_button2.pack()`
  - **Explanation:** Packs the radio button widget into the root window.

### Comments

- Tkinter provides a variety of widgets for building graphical user interfaces, including labels, buttons, entry fields, text areas, frames, check buttons, and radio buttons.
- Widgets can be customized with various options and parameters to control their appearance and behavior.
- Widgets are typically added to a window using the `pack()` method, which organizes them in a vertical or horizontal layout.
- The `command` parameter of a button widget can be used to specify a function to call when the button is clicked.
- Variables such as `StringVar` can be used to link widgets together and synchronize their values.

