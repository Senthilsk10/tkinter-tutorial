## Tkinter GUI Application Example

This repository contains a simple example of creating a GUI (Graphical User Interface) application using Tkinter in Python.

### Code Explanation

- **Syntax:** `from tkinter import *`
  - **Explanation:** Imports all symbols from the `tkinter` module. This allows us to use Tkinter classes and functions without prefixing them with `tk.`.

- **Syntax:** `root = Tk()`
  - **Explanation:** Creates the main application window.

- **Syntax:** `root.geometry("1080x720")`
  - **Explanation:** Sets the initial size of the window to 1080 pixels wide and 720 pixels high.

- **Syntax:** `btn = Button(root, text="click me", command=print("clicked"))`
  - **Explanation:** Creates a button widget with the specified text label "click me". The `command` parameter is assigned to `print("clicked")`, which means that the print statement will be executed immediately when the button is created rather than when it's clicked. To fix this, you should pass a function to `command` instead of calling `print()` directly.

- **Syntax:** `btn.pack()`
  - **Explanation:** Adds the button to the root window using the `pack()` method. This method organizes widgets in blocks before placing them in the parent widget.
