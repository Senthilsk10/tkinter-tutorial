## Tkinter GUI Application Example

This repository contains a simple example of creating a GUI (Graphical User Interface) application using Tkinter in Python.

### Code Explanation

- **Syntax:** `from tkinter import *`
  - **Explanation:** Imports all symbols from the `tkinter` module. This allows us to use Tkinter classes and functions without prefixing them with `tk.`.

- **Syntax:** `root = Tk()`
  - **Explanation:** Creates the main application window.

- **Syntax:** `root.title("example app")`
  - **Explanation:** Sets the title of the window to "example app".

- **Syntax:** `root.geometry("480x480")`
  - **Explanation:** Sets the initial size of the window to 480 pixels wide and 480 pixels high.

- **Syntax:** `Label(root, text="label 1", bg="lightblue").pack(side="top")`
  - **Explanation:** Creates a label widget with the specified text "label 1" and background color "lightblue", then packs it into the root window at the top side.

- **Syntax:** `Label(root, text="label 2").pack(side="left")`
  - **Explanation:** Creates a label widget with the specified text "label 2" and packs it into the root window at the left side.

- **Syntax:** `Label(root, text="label 3").pack(side="right")`
  - **Explanation:** Creates a label widget with the specified text "label 3" and packs it into the root window at the right side.

- **Syntax:** `Button(root, text="label 4").pack(side="bottom", fill='x')`
  - **Explanation:** Creates a button widget with the specified text "label 4" and packs it into the root window at the bottom side. The `fill='x'` parameter specifies that the button should fill the entire width of its container.

- **Syntax:** `Button(root, text="label 5").pack(side="top")`
  - **Explanation:** Creates a button widget with the specified text "label 5" and packs it into the root window at the top side.

### Comments
  - We can stack the widgets one on top of the other using the `pack()` method and specify the side where each widget should be placed (`side="top"`, `side="bottom"`, `side="left"`, `side="right"`).
  - The `fill` parameter of the `pack()` method can be used to specify how the widget should fill its allocated space (`fill='x'` fills horizontally, `fill='y'` fills vertically, `fill='both'` fills both horizontally and vertically).

